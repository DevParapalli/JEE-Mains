import shutil

import requests

from .constants import BASE_DIR, CONFIG



def download_latest_answer_key(shift_code):
    """ Downloads a prepared answer key from a repo"""    
    with open('./temp/answer_key.json', "wb") as answer_key_file:
        answer_key = requests.get('https://raw.githubusercontent.com/DevParapalli/JEE-Mains-AnswerKeys/main/' + shift_code + ".json")
        answer_key.raise_for_status()
        answer_key_file.write(answer_key.content)
    # We update and save the file here. 
    shutil.copy(BASE_DIR /'temp'/'answer_key.json', BASE_DIR / 'save_answer_key_here' / (shift_code +'.json'))

def create_answer_key_lookup_table():
    """ Creates an answer_key from scratch. """
    raise NotImplementedError
