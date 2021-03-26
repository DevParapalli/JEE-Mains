import json
import requests
from jee_mains import response_sheet, answer_key, constants, calculation


BASE_DIR = constants.BASE_DIR
CONFIG = constants.CONFIG


def create_response_sheet():
    return response_sheet.create_response_sheet_json()


def create_answer_key(shift_code):
    if CONFIG['cache_mode'] == "online-only":
        try:
            return answer_key.online_only(shift_code)
        except requests.exceptions.HTTPError:
            print('[E] Answer Key not Found. Please check your shift code or contact EMAIL:devparapalli@gmail.com')

    elif CONFIG['cache_mode'] == "offline-only":
        try:
            return answer_key.offline_only(shift_code)
        except FileNotFoundError:
            print('[E] Answer Key not Found. Please check your shift code or change to online-only or normal mode.')
    
    elif CONFIG['cache_mode'] == "normal":
        return answer_key.normal(shift_code)


def main():
    # Update the notice as the development progresses.
    print(constants.NOTICE)
    shift_code, response_sheet = create_response_sheet()
    answer_key = create_answer_key(shift_code)
    data = calculation.calculate(response_sheet, answer_key)
    result_str = constants.RESULT
    print_data = data['__INF__']
    print(result_str.format(
        name=print_data['Candidate Name'],
        admn=print_data['Application No'],
        roll=print_data['Roll No.'],
        tdte=print_data['Test Date'],
        ttim=print_data['Test Time'],
        subj=print_data['Subject'],
        mark=print_data['Marks'],
        shft=print_data["shift_code"]
    ))
    print('Check Result in Results folder for more details.')
    print('[Program Finished]')

if __name__ == "__main__":
    main()
