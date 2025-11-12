# app_secure.py — Housypoint Secure Assessment (one-question, anti-cheat)
import uuid
from datetime import datetime, timedelta

import streamlit as st
import pandas as pd

# JS bridge for browser visibility / focus (used for anti-cheat)
# install via requirements: streamlit-js-eval
from streamlit_js_eval import streamlit_js_eval

from questions_50 import (
    TEST_DURATION_MIN, PASS_MARK, MCQ_MARKS, LONG_MARKS,
    MCQ_SECTIONS, LONG_QUESTIONS, ANSWER_KEY
)

# ---------- CONFIG ----------
st.set_page_config(page_title="Housypoint Secure Test", page_icon="🧰", layout="centered")
DATA_FILE = "secure_submissions.csv"
ADMIN_KEY = "housypoint-admin-123"   # change if you want

# ---------- STYLES ----------
PRIMARY = "#0B74DE"
st.markdown(f"""
<style>
.hp-card {{ border:1px solid #e5e7eb; padding:16px; border-radius:12px; margin:12px 0; }}
.hp-blur {{ filter: blur(6px); pointer-events:none; opacity:0.8; }}
.timer {{ position:fixed; top:12px; right:18px; background:#eaf3ff; border:1px solid #cfe2ff; padding:6px 10px; border-radius:12px; font-weight:700; color:{PRIMARY}; z-index:999; }}
</style>
""", unsafe_allow_html=True)

# ---------- SESSION INIT ----------
def init():
    ss = st.session_state
    ss.setdefault("uid", str(uuid.uuid4())[:8])
    ss.setdefault("started", False)
    ss.setdefault("deadline", None)
    ss.setdefault("current_index", 0)
    ss.setdefault("answers_mcq", {})
    ss.setdefault("answers_long", {})
    ss.setdefault("locked_until", -1)
    ss.setdefault("warnings", 0)
    ss.setdefault("terminated", False)
    ss.setdefault("submitted", False)
    ss.setdefault("name", "")
    ss.setdefault("empid", "")
    ss.setdefault("mobile", "")
    ss.setdefault("email", "")

init()

# ---------- TIMER ----------
def start_timer():
    if st.session_state.deadline is None:
        st.session_state.deadline = datetime.utcnow() + timedelta(minutes=TEST_DURATION_MIN)

def time_left():
    if st.session_state.deadline is None:
        return "60:00", 3600
    delta = st.session_state.deadline - datetime.utcnow()
    secs = max(0, int(delta.total_seconds()))
    m, s = secs//60, secs%60
    return f"{m:02d}:{s:02d}", secs

tstr, tsecs = time_left()
st.markdown(f'<div class="timer">⏱ {tstr}</div>', unsafe_allow_html=True)
if tsecs == 0 and not st.session_state.submitted and not st.session_state.terminated:
    st.session_state.terminated = True

# ---------- ANTI-CHEAT (visibility/fullscreen) ----------
try:
    vis = streamlit_js_eval(js_expressions="document.visibilityState", key="vis")
except Exception:
    vis = "visible"

if st.session_state.started and not st.session_state.submitted and not st.session_state.terminated:
    if vis != "visible":
        st.session_state.warnings += 1
        if st.session_state.warnings == 1:
            st.warning("⚠️ Warning: You switched tabs/minimized. One more time will terminate the test.")
        elif st.session_state.warnings >= 2:
            st.session_state.terminated = True
            st.error("❌ Cheater detected. Test terminated and answers saved.")

# ---------- PRE-FLIGHT ----------
st.title("Housypoint Secure Inspection Assessment — 50 Questions")
st.caption("One-question mode • No backtracking • 60-minute timer")

if not st.session_state.started:
    with st.form("pref"):
        st.subheader("Candidate details (required to start)")
        st.session_state.name = st.text_input("Full name", value=st.session_state.name)
        st.session_state.empid = st.text_input("Employee ID", value=st.session_state.empid)
        st.session_state.mobile = st.text_input("Mobile (10 digits)", value=st.session_state.mobile)
        st.session_state.email  = st.text_input("Email", value=st.session_state.email)
        st.write("By starting the test you agree to the one-question rules.")
        start = st.form_submit_button("Start Test")
        if start:
            import re
            ok_mobile = bool(re.fullmatch(r"[6-9]\d{9}", st.session_state.mobile.strip()))
            ok_email = bool(re.fullmatch(r"[^@\\s]+@[^@\\s]+\\.[^@\\s]+", st.session_state.email.strip()))
            if not (st.session_state.name and st.session_state.empid and ok_mobile and ok_email):
                st.error("Please provide valid Name, Employee ID, 10-digit Mobile and Email.")
            else:
                st.session_state.started = True
                start_timer()
                st.experimental_rerun()

# ---------- HELPERS ----------
def show_mcq(qobj, locked=False):
    classes = "hp-card " + ("hp-blur" if locked else "")
    st.markdown(f'<div class="{classes}">', unsafe_allow_html=True)
    st.markdown(f"**{qobj['id']}**. {qobj['q']}")
    sel_key = f"mcq_{qobj['id']}"
    sel = st.radio("Select one", qobj["opts"], key=sel_key, index=None, disabled=locked, label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)
    return sel

def show_long(qobj, locked=False):
    classes = "hp-card " + ("hp-blur" if locked else "")
    st.markdown(f'<div class="{classes}">', unsafe_allow_html=True)
    st.markdown(f"**{qobj['id']}**. {qobj['prompt']}")
    ta = st.text_area("Your short report", key=f"long_{qobj['id']}", height=140, disabled=locked, label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)
    return ta

def rubric_score(text, keywords):
    if not text:
        return 0, []
    t = text.lower()
    hits = [k for k in keywords if k.lower() in t]
    frac = min(1.0, len(hits)/max(3, len(keywords)//2 or 1))
    return int(round(frac * LONG_MARKS)), hits

def compute_scores():
    mcq_score = 0
    for q in MCQ_SECTIONS:
        sel = st.session_state.answers_mcq.get(q["id"])
        if sel and sel == q["ans"]:
            mcq_score += MCQ_MARKS
    long_score = 0
    for q in LONG_QUESTIONS:
        s,_ = rubric_score(st.session_state.answers_long.get(q["id"], ""), q["keywords"])
        long_score += s
    return mcq_score, long_score, mcq_score + long_score

def finalize(reason="Submitted"):
    mcq_s, long_s, total = compute_scores()
    result = "PASS" if total >= PASS_MARK else "FAIL"
    row = {
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "uid": st.session_state.uid,
        "name": st.session_state.name,
        "employee_id": st.session_state.empid,
        "mobile": st.session_state.mobile,
        "email": st.session_state.email,
        "warnings": st.session_state.warnings,
        "reason": reason,
        "mcq_score": mcq_s,
        "long_score": long_s,
        "total": total,
        "result": result,
    }
    for q in MCQ_SECTIONS:
        row[f"{q['id']}_ans"] = st.session_state.answers_mcq.get(q["id"])
    for q in LONG_QUESTIONS:
        row[f"{q['id']}_text"] = st.session_state.answers_long.get(q["id"], "")
    try:
        df_old = pd.read_csv(DATA_FILE)
        df_new = pd.concat([df_old, pd.DataFrame([row])], ignore_index=True)
    except Exception:
        df_new = pd.DataFrame([row])
    df_new.to_csv(DATA_FILE, index=False)
    st.session_state.submitted = True
    return row

# ---------- TEST FLOW ----------
if st.session_state.started and not st.session_state.submitted:

    order = [*MCQ_SECTIONS, *LONG_QUESTIONS]
    total_q = len(order)
    idx = st.session_state.current_index

    # show previous (locked)
    if idx > 0:
        prev = order[idx-1]
        st.markdown("**Previous (locked)**")
        if "opts" in prev:
            show_mcq(prev, locked=True)
        else:
            show_long(prev, locked=True)

    st.markdown(f"**Question {idx+1} of {total_q}**")
    cur = order[idx]
    if "opts" in cur:
        sel = show_mcq(cur)
        if sel is not None:
            st.session_state.answers_mcq[cur["id"]] = sel
    else:
        ta = show_long(cur)
        st.session_state.answers_long[cur["id"]] = ta

    cols = st.columns([1,1,1])
    with cols[0]:
        if st.button("Lock & Next ➜"):
            # require answer
            if "opts" in cur:
                if st.session_state.answers_mcq.get(cur["id"]) is None:
                    st.warning("Please select an option to proceed.")
                    st.stop()
            else:
                if len((st.session_state.answers_long.get(cur["id"], "") or "").strip()) == 0:
                    st.warning("Please write a short answer to proceed.")
                    st.stop()
            st.session_state.locked_until = idx
            if idx < total_q - 1:
                st.session_state.current_index = idx + 1
                st.experimental_rerun()
            else:
                # last Q -> finalize
                row = finalize("Completed")
                st.success(f"Test Completed. Total {row['total']} (MCQ {row['mcq_score']} + Long {row['long_score']})")
    with cols[1]:
        if st.button("Submit Now"):
            row = finalize("Manual submit")
            st.success(f"Submitted. Total {row['total']}")
    with cols[2]:
        if st.button("Exit (forfeit)"):
            st.session_state.terminated = True

# ---------- TERMINATION ----------
if st.session_state.terminated and not st.session_state.submitted:
    row = finalize("Terminated (cheat/timeout/exit)")
    st.error("Test terminated. Answers saved.")
    st.write(f"Score: {row['total']}")

# ---------- POST SUBMIT ----------
if st.session_state.submitted:
    st.success("Your submission is recorded.")
    mcq, lng, tot = compute_scores()
    st.metric("Total", tot)
    st.metric("MCQ", mcq)
    st.metric("Long", lng)
    st.download_button("⬇️ Download your acknowledgement", data=pd.DataFrame([{
        "uid": st.session_state.uid, "name": st.session_state.name, "employee_id": st.session_state.empid, "total": tot
    }]).to_csv(index=False), file_name=f"{st.session_state.empid}_{st.session_state.uid}.csv", mime="text/csv")

# ---------- ADMIN PANEL ----------
st.divider()
st.subheader("🔐 Admin Panel")
key = st.text_input("Enter Admin Key", type="password")
if key == ADMIN_KEY:
    st.success("Admin access granted.")
    try:
        df = pd.read_csv(DATA_FILE)
        st.dataframe(df, use_container_width=True, height=420)
        st.download_button("⬇️ Download all (CSV)", df.to_csv(index=False), file_name="secure_submissions.csv", mime="text/csv")
    except FileNotFoundError:
        st.info("No submissions yet.")
elif key:
    st.error("Invalid admin key.")
