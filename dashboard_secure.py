# dashboard_secure.py — Analytics for Housypoint Secure Assessment
import streamlit as st
import pandas as pd
from questions_50 import ANSWER_KEY, MCQ_SECTIONS, PASS_MARK

st.set_page_config(page_title="Housypoint Test Dashboard", page_icon="📊", layout="wide")
DATA_FILE = "secure_submissions.csv"

st.title("📊 Housypoint Test Dashboard (Secure)")

@st.cache_data
def load_data(path: str):
    df = pd.read_csv(path)
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    for c in ["mcq_score","long_score","total","warnings"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

try:
    df = load_data(DATA_FILE)
except FileNotFoundError:
    st.info("No submissions found yet. After first submission this dashboard will populate.")
    st.stop()

if df.empty:
    st.info("No submissions yet.")
    st.stop()

# Sidebar filters
with st.sidebar:
    st.header("Filters")
    dmin, dmax = df["timestamp"].min().date(), df["timestamp"].max().date()
    dr = st.date_input("Date range", value=(dmin, dmax))
    if isinstance(dr, tuple) and len(dr) == 2:
        df = df[(df["timestamp"].dt.date >= dr[0]) & (df["timestamp"].dt.date <= dr[1])]
    q = st.text_input("Search name/ID/mobile/email").strip().lower()
    if q:
        df = df[
            df["name"].str.lower().str.contains(q, na=False)
            | df["employee_id"].astype(str).str.lower().str.contains(q, na=False)
            | df["mobile"].astype(str).str.contains(q, na=False)
            | df["email"].astype(str).str.contains(q, na=False)
        ]
    warn_min = st.slider("Show warnings ≥", 0, int(df["warnings"].max() or 0), 0)
    df = df[df["warnings"] >= warn_min]

# KPIs
total_candidates = len(df)
pass_count = int((df["total"] >= PASS_MARK).sum())
fail_count = total_candidates - pass_count
top_score = int(df["total"].max())
low_score = int(df["total"].min())
avg_score = round(df["total"].mean(), 2)

c1,c2,c3,c4,c5 = st.columns(5)
c1.metric("Total Submissions", total_candidates)
c2.metric("Pass", pass_count)
c3.metric("Fail", fail_count)
c4.metric("Top Score", top_score)
c5.metric("Average Score", avg_score)

st.markdown("---")

# Charts
colA,colB = st.columns(2)
with colA:
    st.subheader("Score distribution")
    st.bar_chart(df["total"])
with colB:
    st.subheader("Pass vs Fail")
    pf = pd.DataFrame({"Status":["Pass","Fail"], "Count":[pass_count, fail_count]}).set_index("Status")
    st.bar_chart(pf)

# Top & Underperformers
st.subheader("Top & Underperformers")
left,right = st.columns(2)
with left:
    st.caption("Top 10")
    st.dataframe(df.sort_values(["total","timestamp"], ascending=[False, True]).head(10)[["timestamp","name","employee_id","mobile","email","total","warnings"]], use_container_width=True)
with right:
    st.caption("Underperformers (below pass)")
    st.dataframe(df[df["total"] < PASS_MARK].sort_values("total")[["timestamp","name","employee_id","mobile","email","total","warnings"]], use_container_width=True)

# Per-question accuracy
st.subheader("Per-question Accuracy (MCQs)")
mcq_ids = [q["id"] for q in MCQ_SECTIONS]
present = [f"{qid}_ans" for qid in mcq_ids if f"{qid}_ans" in df.columns]
if present:
    rows = []
    for qid in mcq_ids:
        col = f"{qid}_ans"
        if col not in df.columns: continue
        total = df[col].notna().sum()
        correct = (df[col] == ANSWER_KEY.get(qid)).sum()
        acc = round(100 * correct / total, 1) if total else 0.0
        rows.append({"Question": qid, "Answered": int(total), "Correct": int(correct), "Accuracy %": acc})
    acc_df = pd.DataFrame(rows)
    st.dataframe(acc_df, use_container_width=True)
    st.bar_chart(acc_df.set_index("Question")["Accuracy %"])
else:
    st.info("Per-question columns not yet present in CSV.")

# Raw table & export
st.subheader("All submissions (raw)")
st.dataframe(df.sort_values("timestamp", ascending=False), use_container_width=True, height=420)
st.download_button("⬇️ Download CSV", df.to_csv(index=False), "secure_submissions.csv", "text/csv")
