import json
import string

from .correction_to_answer_key import BASE_DIR, CONFIG

IGNORE_LINES_STARTSWITH = tuple([letter for letter in string.ascii_letters + "!@#$%^&*(" + "  "])

LANG = {
    "Urdu": "UDU",
    "Assamese": "ASM",
    "Bengali": "BEN",
    "English": "ENG",
    "Gujarati": "GUJ",
    "Hindi": "HIN",
    "Kannada": "KAN",
    "Malayalam": "MAL",
    "Marathi": "MAR",
    "Odia": "ODA",
    "Punjabi": "PUN",
    "Tamil": "TML",
    "Telugu": "TGU",
}


def get_filename(answer_key):
    lines = answer_key.split('\n')

    # Date Logic
    # Exam Date : 26.02.2021 Course : B.E./B.Tech Medium : English
    date_line = lines[0]
    data_alpha = [portion.strip() for portion in date_line.split(":")]
    date_str = data_alpha[1].replace("Course", "").strip()
    day, month, year = [part.strip() for part in date_str.split(".")]

    # Course Logic
    course_str = data_alpha[2].replace("Medium", "").strip()
    subject = "TECH" if course_str.find('Tech') != -1 else "PLAN"

    # Language Logic
    language_str = data_alpha[3].strip()
    lang = LANG[language_str]

    # Shift timing Logic
    shift_line = lines[2]
    shift = "M" if shift_line.find("First") != -1 else "E"

    filename = "-".join((year, month, day, shift, lang, subject))
    return filename


with open(BASE_DIR / '__internals__' / 'shift_code.txt') as file:
    __split = file.read().split("Exam Date")
    answer_keys = ["Exam Date" + portion for portion in __split]
    # First one is borked since it contains the header for the page.
    for answer_key in answer_keys[1:]:
        file_name = get_filename(answer_key)
        with open(BASE_DIR / "__internals__" / "output" / (file_name +".json"), "w") as file:
            ANSWERS = {}
            for line in answer_key.split('\n'):
                # Skip if line doesn't contain question answer pair
                if line.startswith(IGNORE_LINES_STARTSWITH): continue 
                # Skip if line blank
                if line == "": continue 
                question, answer = line.split()
                ANSWERS[question] = answer
            file.write(json.dumps(ANSWERS))
