import json
import requests
from jee_mains import response_sheet, answer_key, constants, calculation

BASE_DIR = constants.BASE_DIR

def create_response_sheet():
    response_sheet.create_response_sheet_json()
    
def create_answer_key():
    with open(BASE_DIR / 'config.json') as file:
        CONFIG = json.loads(file.read())
    shift_code = CONFIG["shift_code"]
    try:
        answer_key.download_latest_answer_key(shift_code)
    except requests.exceptions.HTTPError:
        print('[E] Answer Key not Found. Please check your shift code or contact EMAIL:devparapalli@gmail.com')


def main():
    # Update the notice as the development progresses.
    print(constants.NOTICE) 
    print("[I] Parsing Response Sheet")
    create_response_sheet()
    print("[D] Downloading latest Answer Key")
    create_answer_key()
    with open(BASE_DIR / 'temp' / 'parsed_response_sheet.json') as response_file:
        response_sheet = json.loads(response_file.read())
    with open(BASE_DIR / 'temp' / 'answer_key.json') as answer_file:
        answer_key = json.loads(answer_file.read())
    data = calculation.calculate(response_sheet, answer_key)
    result_str = constants.RESULT
    print(result_str.format(
        name=data['__INF__']['Candidate Name'],
        admn=data['__INF__']['Application No'],
        roll=data['__INF__']['Roll No.'],
        tdte=data['__INF__']['Test Date'],
        ttim=data['__INF__']['Test Time'],
        subj=data['__INF__']['Subject'],
        mark=data['__INF__']['Marks'],
    ))
    print('Check ./temp/final_results.json for more details.')
    print('[Program Finished]')
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print('[E] Segmentation Fault')
        raise e 