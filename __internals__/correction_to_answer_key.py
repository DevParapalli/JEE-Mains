import bs4
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

with open(BASE_DIR / 'config.json') as file:
    CONFIG = json.loads(file.read())

# The {} can range from 00 to 200 will parse all of it 
HTML_ID = {
    #"application_number":"ctl00_LoginContent_lblAppno",
    #"roll_number":"ctl00_LoginContent_lblRollno",
    #"name":"ctl00_LoginContent_lblName",
    #"father_name":"ctl00_LoginContent_lblFname",
    #"mother_name":"ctl00_LoginContent_lblMName",
    #"date_of_birth":"ctl00_LoginContent_lblDob",
    "subject_id_format":"ctl00_LoginContent_grAnswerKey_ctl{}_lblsubject",
    "question_type_format":"ctl00_LoginContent_grAnswerKey_ctl{}_lbl_QuestionTypeTitle",
    "question_id_format":"ctl00_LoginContent_grAnswerKey_ctl{}_lbl_QuestionNo",
    "answer_id_format":"ctl00_LoginContent_grAnswerKey_ctl{}_lbl_RAnswer",
    "":"",
}

## VARIABLES TO EDIT
FILENAME = 'shift_code.html'
PATH_TO_CORRECTION_HTML = BASE_DIR / '__internals__' / FILENAME
PATH_TO_OUTPUT_JSON = BASE_DIR / '__internals__' / (FILENAME.split('.')[0] + ".json")

with open(PATH_TO_CORRECTION_HTML) as file:
    SOUP = bs4.BeautifulSoup(file.read(), features='html5lib')

QUESTIONS = {}
for i in range(0, 200):
    if i in range(0, 10): i = "0" + str(i)
    try: 
        question_id = str(SOUP.find('span', id=HTML_ID["question_id_format"].format(i)).string).strip()
        answer_id = str(SOUP.find('span', id=HTML_ID["answer_id_format"].format(i)).string).strip()
        QUESTIONS[question_id] = answer_id
    except AttributeError:
        continue

with open(PATH_TO_OUTPUT_JSON, "w") as file:
    file.write(json.dumps(QUESTIONS))

