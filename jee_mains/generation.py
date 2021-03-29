""" Generates HTML Result from Questions """

from .constants import BASE_DIR, CONFIG
from .template import TEMPLATE
import json


def generate(QUESTIONS_DICT):
    INFO = QUESTIONS_DICT["__INF__"]


#         [key for key in DICT]
    PSC = {question for question in QUESTIONS_DICT['PSC']}
    PSN = {question for question in QUESTIONS_DICT['PSN']}
    PSL = {question for question in QUESTIONS_DICT['PSL']}

    PIC = {question for question in QUESTIONS_DICT['PIC']}
    PIN = {question for question in QUESTIONS_DICT['PIN']}
    PIL = {question for question in QUESTIONS_DICT['PIL']}

    CSC = {question for question in QUESTIONS_DICT['CSC']}
    CSN = {question for question in QUESTIONS_DICT['CSN']}
    CSL = {question for question in QUESTIONS_DICT['CSL']}

    CIC = {question for question in QUESTIONS_DICT['CIC']}
    CIN = {question for question in QUESTIONS_DICT['CIN']}
    CIL = {question for question in QUESTIONS_DICT['CIL']}

    MSC = {question for question in QUESTIONS_DICT['MSC']}
    MSN = {question for question in QUESTIONS_DICT['MSN']}
    MSL = {question for question in QUESTIONS_DICT['MSL']}

    MIC = {question for question in QUESTIONS_DICT['MIC']}
    MIN = {question for question in QUESTIONS_DICT['MIN']}
    MIL = {question for question in QUESTIONS_DICT['MIL']}

    rendered_page = TEMPLATE.format(
        styles="@media print{ .no-print{visibility:hidden}}",
        name=INFO["Candidate Name"],
        admission_number=INFO["Application No"],
        roll_number=INFO["Roll No."],
        test_date=INFO["Test Date"],
        test_time=INFO["Test Time"],
        subject=INFO["Subject"],
        marks_obtained=INFO["Marks"],
        shift_code=INFO["shift_code"],
        total_correct=INFO["correct"],
        total_incorrect=INFO["incorrect"],
        total_left=INFO["left"],
        physics_scq_correct="<br>".join(PSC),
        physics_scq_incorrect="<br>".join(PSN),
        physics_scq_left="<br>".join(PSL),
        physics_int_correct="<br>".join(PIC),
        physics_int_incorrect="<br>".join(PIN),
        physics_int_left="<br>".join(PIL),
        chemistry_scq_correct="<br>".join(CSC),
        chemistry_scq_incorrect="<br>".join(CSN),
        chemistry_scq_left="<br>".join(CSL),
        chemistry_int_correct="<br>".join(CIC),
        chemistry_int_incorrect="<br>".join(CIN),
        chemistry_int_left="<br>".join(CIL),
        maths_scq_correct="<br>".join(MSC),
        maths_scq_incorrect="<br>".join(MSN),
        maths_scq_left="<br>".join(MSL),
        maths_int_correct="<br>".join(MIC),
        maths_int_incorrect="<br>".join(MIN),
        maths_int_left="<br>".join(MIL),
        raw_json="You expected something here? Go turn on DEBUG" if not CONFIG["DEBUG"] else json.dumps(QUESTIONS_DICT, indent=4)
    )
    with open(BASE_DIR / 'Results' / (INFO["Application No"] + INFO["shift_code"] + ".html"), "w", encoding="utf-16") as file:
        file.write(rendered_page)
