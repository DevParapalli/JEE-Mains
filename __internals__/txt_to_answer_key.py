import json
import string

from correction_to_answer_key import BASE_DIR, CONFIG

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


def get_subject(course_string):
    if course_string.find("Tech") != -1: return 'TECH'
    if course_string.find("Planning") != -1 and course_string.find('Arch') == -1: return "PLAN"
    if course_string.find("Planning") == -1 and course_string.find('Arch') != -1: return "ARCH"
    if course_string.find("Planning") != -1 and course_string.find('Arch') != -1: return "PLAR"
    else: return "UKN"
def get_filename(answer_key):
    lines = answer_key.split('\n')

    # Date Logic
    # Exam Date : 26.02.2021 Course : B.E./B.Tech Medium : English 
    # Medium is not always present. Use English as a default.
    date_line = lines[0]
    data_alpha = [portion.strip() for portion in date_line.split(":")]
    date_str = data_alpha[1].replace("Course", "").strip()
    day, month, year = [part.strip() for part in date_str.split(".")]

    # Course Logic
    course_str = data_alpha[2].replace("Medium", "").strip()
    subject = get_subject(course_str)

    # Language Logic
    try:
        language_str = data_alpha[3].strip()
    except IndexError: 
        language_str = "English"

    lang = LANG[language_str]

    # Shift timing Logic
    shift_line = lines[2]
    shift = "M" if shift_line.find("First") != -1 else "E"

    filename = "-".join((year, month, day, shift, lang, subject))
    return filename

def main(string):
    with open(BASE_DIR / '__internals__' / (string + '.txt')) as file:
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
                    question, answer = line.split(maxsplit=1)
                    ANSWERS[question] = answer
                file.write(json.dumps(ANSWERS))
                
if __name__ == "__main__":
    main("march_final")
