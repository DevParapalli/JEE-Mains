import json
import requests
from jee_mains import response_sheet, answer_key, constants, calculation

BASE_DIR = constants.BASE_DIR
CONFIG = constants.CONFIG


def create_response_sheet():
    response_sheet.create_response_sheet_json()


def create_answer_key():
    shift_code = CONFIG["shift_code"]
    if CONFIG['cache_mode'] == "online-only":
        try:
            answer_key.online_only(shift_code)
        except requests.exceptions.HTTPError:
            print('[E] Answer Key not Found. Please check your shift code or contact EMAIL:devparapalli@gmail.com')

    elif CONFIG['cache_mode'] == "offline-only":
        try:
            answer_key.offline_only(shift_code)
        except FileNotFoundError:
            print('[E] Answer Key not Found. Please check your shift code or change to online-only or normal mode.')
    
    elif CONFIG['cache_mode'] == "normal":
        answer_key.normal(shift_code)


def main():
    # Update the notice as the development progresses.
    print(constants.NOTICE)
    create_response_sheet()
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
    main()
