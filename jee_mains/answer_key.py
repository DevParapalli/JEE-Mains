import shutil

import requests


def download_latest_answer_key(shift_code):
    """ Downloads a prepared answer key from a repo"""
    with open('./temp/answer_key.json', "wb") as answer_key_file:
        answer_key_file.write(requests.get(
            'https://raw.githubusercontent.com/DevParapalli/JEE-Mains-AnswerKeys/main/' + shift_code + ".json").content)
    # We update and save the file here. 
    shutil.copy('./temp/answer_key.json', './answer_key/answer_key.json')

def create_answer_key_lookup_table():
    
    raise NotImplementedError
