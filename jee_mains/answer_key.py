import json
import os


import requests

from .constants import BASE_DIR

answer_key_ext = ".json"

def online_only(shift_code):
    """ Downloads a prepared answer key from a repo"""    
    #//print("[D] Downloading latest Answer Key")
    answer_key = requests.get('https://raw.githubusercontent.com/DevParapalli/JEE-Mains-AnswerKeys/main/' + shift_code + answer_key_ext)
    answer_key.raise_for_status()
    return answer_key.json()
    # Removed logic for saving the file.
    #shutil.copy(BASE_DIR /'temp'/'answer_key.json', BASE_DIR / 'answer_key_storage' / (shift_code +'.json'))

def create_answer_key_lookup_table():
    """ Creates an answer_key from scratch. """
    raise NotImplementedError

def offline_only(shift_code):
    if os.path.exists(BASE_DIR / 'answer_key_storage' / (shift_code + answer_key_ext)):
        #//print("[I] Selecting Answer Key")
        return json.loads(open(BASE_DIR / 'answer_key_storage' / (shift_code + answer_key_ext)).read())
    else: raise FileNotFoundError

def normal(shift_code):
    try:
        return offline_only(shift_code)
    except FileNotFoundError:
        #//print("[E] File Not Found, Downloading")
        return online_only(shift_code)
