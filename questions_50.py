# questions_50.py
# Housypoint Secure Assessment – 50 Questions (45 MCQ + 5 Short Answer)
# Edit this file whenever you want to change questions.

# ------------- MARKING & TEST SETTINGS -------------
TEST_DURATION_MIN = 60  # minutes
PASS_MARK = 30
MCQ_MARKS = 1
LONG_MARKS = 3

# ------------- SECTIONS -------------
# A: 20 Basic Civil Engineering MCQs
BASIC_CIVIL = [
    {"id":"A1","q":"Initial setting time of OPC (approx.):","opts":["10 min","30 min","60 min","90 min"],"ans":"30 min"},
    {"id":"A2","q":"Most common test for concrete workability:","opts":["Vee-Bee","Compaction factor","Slump test","Flow table"],"ans":"Slump test"},
    {"id":"A3","q":"Standard cube size for compressive strength test:","opts":["100 mm","150 mm","200 mm","300 mm"],"ans":"150 mm"},
    {"id":"A4","q":"Typical curing period often used for good strength (days):","opts":["3–5 days","7 days","14 days","28 days"],"ans":"14 days"},
    {"id":"A5","q":"Bulking of sand is mainly due to:","opts":["Clay content","Moisture films","Silt content","Grading"],"ans":"Moisture films"},
    {"id":"A6","q":"Recommended cement for aggressive marine exposure:","opts":["OPC 33","PPC","SRC","Rapid hardening cement"],"ans":"SRC"},
    {"id":"A7","q":"Increasing water–cement ratio generally:","opts":["Increases strength","Reduces strength","No change","Doubles strength"],"ans":"Reduces strength"},
    {"id":"A8","q":"Common brick class for load bearing masonry:","opts":["Class 50","Class 35","Class 20","Class 10"],"ans":"Class 35"},
    {"id":"A9","q":"IS sieve size used to separate fine aggregate:","opts":["4.75 mm","10 mm","2.36 mm","1.18 mm"],"ans":"4.75 mm"},
    {"id":"A10","q":"Minimum compressive strength of M20 concrete (28 d):","opts":["15 MPa","20 MPa","25 MPa","30 MPa"],"ans":"20 MPa"},
    {"id":"A11","q":"Best vibrator type for slab compaction:", "opts":["Plate vibrator","Needle vibrator","Tamping rod","Roller"], "ans":"Needle vibrator"},
    {"id":"A12","q":"Purpose of entrained air in concrete:","opts":["Increase density","Improve workability & frost resistance","Reduce setting time","Increase heat"],"ans":"Improve workability & frost resistance"},
    {"id":"A13","q":"Efflorescence in masonry is caused by:", "opts":["Soluble salts","Low sand","High cement","Over curing"], "ans":"Soluble salts"},
    {"id":"A14","q":"Where is DPC normally provided?","opts":["Plinth level","Roof level","Foundation base","Floor finish"],"ans":"Plinth level"},
    {"id":"A15","q":"Preferred timber seasoning method for quality:", "opts":["Kiln","Sun dry","Water seasoning","No seasoning"], "ans":"Kiln"},
    {"id":"A16","q":"Specific gravity of ordinary Portland cement (approx):", "opts":["2.1","2.5","3.15","3.6"], "ans":"3.15"},
    {"id":"A17","q":"Max aggregate size commonly used for slab:", "opts":["10 mm","20 mm","40 mm","63 mm"], "ans":"20 mm"},
    {"id":"A18","q":"Bleeding in concrete means:", "opts":["Loss of cement","Water rising to surface","Aggregate segregation","Rapid setting"], "ans":"Water rising to surface"},
    {"id":"A19","q":"Quick on-site non-destructive test for concrete strength:", "opts":["Ultrasonic pulse velocity","Core cutting","Rebound hammer","Half-cell"], "ans":"Rebound hammer"},
    {"id":"A20","q":"Best action when sand is heavily bulking:", "opts":["Dry sand before use","Add more cement","Use more water","Reduce sand"], "ans":"Dry sand before use"},
]

# B: 10 Home Inspection MCQs
HOME_INSPECTION = [
    {"id":"B1","q":"Hollow sound when tapping a tile usually indicates:","opts":["Poor bonding/air gap","Bad glaze","Over grouting","Paint issue"],"ans":"Poor bonding/air gap"},
    {"id":"B2","q":"Best on-site tool to measure carpet area accurately:","opts":["Measuring tape only","Moisture meter","Laser distance meter","Ruler"],"ans":"Laser distance meter"},
    {"id":"B3","q":"Paint blistering near skirting is commonly due to:","opts":["Rising damp","UV failure","Dust","High VOC paint"],"ans":"Rising damp"},
    {"id":"B4","q":"Before conducting bathroom water test you should:","opts":["Close drains","Check slope & outlet direction","Grout all joints","Apply paint"],"ans":"Check slope & outlet direction"},
    {"id":"B5","q":"Efflorescence on tiles suggests:","opts":["Algae","Water ingress from behind","Bad primer","Over-curing"],"ans":"Water ingress from behind"},
    {"id":"B6","q":"Gaps around UPVC window frames should be sealed with:","opts":["POP","PU/Silicone sealant","Cement slurry","Paint"],"ans":"PU/Silicone sealant"},
    {"id":"B7","q":"Ceiling damp below an upper toilet often indicates:","opts":["Condensation","Concealed pipe/trap leak","Openable window","Electrical fault"],"ans":"Concealed pipe/trap leak"},
    {"id":"B8","q":"Carpet area calculation excludes:","opts":["Internal walls","External walls","Balcony","All of these"],"ans":"All of these"},
    {"id":"B9","q":"To confirm active dampness, use:","opts":["Infrared thermometer","Moisture meter","Lux meter","Sound meter"],"ans":"Moisture meter"},
    {"id":"B10","q":"Minor wall waviness is best fixed by:","opts":["Full replaster","Skim coat/putty & sanding","Power washing","Only paint"],"ans":"Skim coat/putty & sanding"},
]

# C: 5 RCC MCQs
RCC = [
    {"id":"C1","q":"Minimum clear cover for slab reinforcement (typical):","opts":["10 mm","15 mm","20 mm","25 mm"],"ans":"20 mm"},
    {"id":"C2","q":"Lapping should be avoided in which zone:","opts":["Mid-span compression","Tension zone near supports","Neutral axis","Any zone"],"ans":"Tension zone near supports"},
    {"id":"C3","q":"Common cause of flexural cracks in slabs:","opts":["Over-reinforcement","Insufficient depth/bars","Too much cover","Over curing"],"ans":"Insufficient depth/bars"},
    {"id":"C4","q":"Development length depends on:","opts":["Bar dia & bond","Concrete grade only","Cover only","Beam size"],"ans":"Bar dia & bond"},
    {"id":"C5","q":"Typical water–cement ratio for M25 grade:","opts":["0.3–0.35","0.4–0.45","0.5–0.55","0.6–0.65"],"ans":"0.4–0.45"},
]

# D: 10 Leakage / case-based MCQs
LEAKAGE = [
    {"id":"D1","q":"Dampness at bedroom wall adjoining toilet wall likely due to:","opts":["Condensation","Capillary from slab base","Concealed line seepage","Exterior rain only"],"ans":"Concealed line seepage"},
    {"id":"D2","q":"Balcony door corner dampness is most often:","opts":["Frame sealant failure","Tile discoloration","Solar gain","Dust"],"ans":"Frame sealant failure"},
    {"id":"D3","q":"Parapet coping cracks allow:","opts":["Air leakage","Water ingress & wall staining","Heat gain","Noise"],"ans":"Water ingress & wall staining"},
    {"id":"D4","q":"Roof drain collar should be:","opts":["Left raw","Sealed with PU & fillet","Painted only","Covered with tape"],"ans":"Sealed with PU & fillet"},
    {"id":"D5","q":"AC indoor drain T-joint concealed inside wall typically causes:","opts":["Noise only","Capillary rise","Leak path into wall chase","Efflorescence only"],"ans":"Leak path into wall chase"},
    {"id":"D6","q":"To verify roof waterproofing you should perform:","opts":["Hammer test","24-hr ponding test","Only visual check","UV test"],"ans":"24-hr ponding test"},
    {"id":"D7","q":"Efflorescence near sill indicates:","opts":["Salt migration due to moisture","Paint overdose","Primer failure","UV burn"],"ans":"Salt migration due to moisture"},
    {"id":"D8","q":"Most reliable joint sealant in wet areas:","opts":["POP + water","Acrylic putty","Silicone/PU","Fevicol"],"ans":"Silicone/PU"},
    {"id":"D9","q":"Recommended slope for terraces toward drain:","opts":["1:60","1:80","1:100–1:120","1:200"],"ans":"1:100–1:120"},
    {"id":"D10","q":"Best filler for dynamic crack at junction:","opts":["Cement slurry","Epoxy grout","PU sealant + backer rod","White cement"],"ans":"PU sealant + backer rod"},
]

# E: 5 Short answer / report-style prompts (keywords for simple rubric)
LONG = [
    {
        "id":"E1",
        "prompt":"Bedroom tile inspection: 5 hollow tiles, 3 stained, 2 cracked near balcony door. Write a short inspection note with location marking method, recommended repair, and materials.",
        "keywords":["hollow","stained","cracked","mark","replace","regrout","epoxy","sealant","photo"]
    },
    {
        "id":"E2",
        "prompt":"Blistering/peeling observed on lower portion of bedroom wall near entrance on 3 sides. Write cause, tests to confirm, and step-by-step repair.",
        "keywords":["rising damp","moisture meter","scrape","biocide","primer","elastomeric","seal"]
    },
    {
        "id":"E3",
        "prompt":"Roof slab waterproofing verification during handover. List checks (surface prep, cracks, upturns), ponding method and acceptance criteria.",
        "keywords":["slope","ponding","24","fillet","drain","coating","upturn","thickness"]
    },
    {
        "id":"E4",
        "prompt":"Toilet inspection: water stagnation near floor trap, slow flow. Give probable reasons and corrective action steps.",
        "keywords":["slope","trap","recess","regrout","clean","test"]
    },
    {
        "id":"E5",
        "prompt":"External wall efflorescence below parapet. Write cause, risk to paint, and preventive maintenance plan.",
        "keywords":["salts","water ingress","primer","breathable","drainage","maintenance"]
    },
]

# ------------- BUNDLE & KEY -------------
MCQ_SECTIONS = BASIC_CIVIL + HOME_INSPECTION + RCC + LEAKAGE  # 45 MCQs
assert len(MCQ_SECTIONS) == 45, "MCQ count must be 45"
LONG_QUESTIONS = LONG
ANSWER_KEY = {q["id"]: q["ans"] for q in MCQ_SECTIONS}
ALL_QUESTIONS = MCQ_SECTIONS + LONG_QUESTIONS
