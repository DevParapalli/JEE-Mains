import shutil

import bs4
import requests

from .constants import CLASS_SELECTORS, CSS_SELECTORS, XPATH


def create_response_sheet_json(download=False):
    raise NotImplementedError

def download_response_sheet_json(url_to_response_sheet):
    """ Incase the response_sheet file is not present or user has explicitly requested it. """
    with open('./temp/response_sheet.html', 'wb') as response_sheet_file:
        response_sheet_file.write(
            requests.get(url_to_response_sheet).content
        )
    # We update and save the file here. Prevents redownloading.
    shutil.copy("./temp/response_sheet.html", "./response_sheet/response_sheet.html") # 


def single_choice_question_handler():
    raise NotImplementedError

def multiple_choice_question_handler():
    raise NotImplementedError

def integer_choice_question_handler():
    raise NotImplementedError
