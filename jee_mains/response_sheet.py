import shutil
import json

import bs4
import requests

from .constants import BASE_DIR


def download_response_sheet_json(url_to_response_sheet):
    """ Incase the response_sheet file is not present or user has explicitly requested it. """
    with open('./temp/response_sheet.html', 'wb') as response_sheet_file:
        response_sheet_file.write(
            requests.get(url_to_response_sheet).content
        )
    # We update and save the file here. Prevents redownloading.
    shutil.copy("./temp/response_sheet.html",
                "./response_sheet/response_sheet.html")


def parse_type(question_soup):
    """ Returns MCQ or SA """  
    # Since this is the first tr, we can just get it, the td with value is always bold
    # We use a different implement here cuz we dont know the question type and cannot rely on length of tr or td
    return question_soup.find('table', class_="menu-tbl").find('tr').find('td', class_="bold").string.__str__().strip()


def single_choice_question_handler(question_soup):
    question_id = str(question_soup.find(class_="menu-tbl").find('tbody').find_all('tr')[1].find_all('td')[-1].string).strip()
    question_data = {"type": "SCQ"}
    # This can be Answered or Not Answered.
    question_data['status'] = str(question_soup.find(class_="menu-tbl").find('tbody').find_all('tr')[-2].find_all('td')[-1].string).strip()
    # This options are all long integers, we keep it as string cuz performance
    question_data['A'] = str(question_soup.find(class_="menu-tbl").find('tbody').find_all('tr')[2].find_all('td')[-1].string).strip()
    question_data['B'] = str(question_soup.find(class_="menu-tbl").find('tbody').find_all('tr')[3].find_all('td')[-1].string).strip()
    question_data['C'] = str(question_soup.find(class_="menu-tbl").find('tbody').find_all('tr')[4].find_all('td')[-1].string).strip()
    question_data['D'] = str(question_soup.find(class_="menu-tbl").find('tbody').find_all('tr')[5].find_all('td')[-1].string).strip()
    # This gives the "Integer" value of the option,
    # The mapping is 1 -> A etc.
    question_data['chosen_option'] = str(question_soup.find(class_="menu-tbl").find('tbody').find_all('tr')[-1].find_all('td')[-1].string).strip()
    option = question_data['chosen_option']
    if option == "1":
        question_data['answer_given'] = question_data['A']
    elif option == "2":
        question_data['answer_given'] = question_data['B']
    elif option == "3":
        question_data['answer_given'] = question_data['C']
    elif option == "4":
        question_data['answer_given'] = question_data['D']

    return question_id, question_data


def multiple_choice_question_handler():
    raise NotImplementedError


def integer_choice_question_handler(question_soup):
    question_id = str(question_soup.find(class_="menu-tbl").find('tbody').find_all('tr')[1].find_all('td')[-1].string).strip()
    # implementation details are given in single_choice_question_handler() and notes.md
    question_data = {"type": "INT"}
    question_data['status'] = str(question_soup.find(class_="menu-tbl").find('tbody').find_all('tr')[-1].find_all('td')[-1].string).strip()
    question_data['answer_given'] = str(question_soup.find(class_="questionRowTbl").find('tbody').find_all('tr')[-1].find_all('td')[-1].string).strip()
    return question_id, question_data


def section_handler(section_soup):
    questions = section_soup.find_all('div', class_="question-pnl")
    return_data = {}
    # We need to only check the first question
    # since the questions are sorted.
    question_type = parse_type(questions[1])
    if question_type == "MCQ":
        for question in questions:
            key, value = single_choice_question_handler(question)
            return_data[key] = value
    elif question_type == "SA":
        for question in questions:
            key, value = integer_choice_question_handler(question)
            return_data[key] = value
    return return_data


def info_panel_handler(info_soup):
    return_data = {}
    for tr in info_soup.find_all('tr'):
        key, value = tr.find_all('td')
        return_data[str(key.string).strip()] = str(value.string).strip()
    return return_data

def create_response_sheet_json(download=False):
    if download: # Do this only if explicitly stated.
        with open(BASE_DIR / 'config.json') as file:
            config = json.loads(file.read())
            url = config['response_sheet_url']
            download_response_sheet_json(url)
    
    with open(BASE_DIR / 'save_response_sheet_here' / 'response_sheet.html') as file:
        soup = bs4.BeautifulSoup(file.read(), features="html5lib")
    # We now successfully have a Soup object
    # This is the object containing all the data.
    response_sheet_content = {}
    # Information Logic
    info_table = soup.find(class_="main-info-pnl")
    response_sheet_content['info'] = info_panel_handler(info_table)
    # for tag in
    # Questions Logic
    sections = soup.find_all(class_="section-cntnr")

    response_sheet_content["physics-single"] = section_handler(sections[0])
    response_sheet_content["physics-integer"] = section_handler(sections[1])
    response_sheet_content["chemistry-single"] = section_handler(sections[2])
    response_sheet_content["chemistry-integer"] = section_handler(sections[3])
    response_sheet_content["maths-single"] = section_handler(sections[4])
    response_sheet_content["maths-integer"] = section_handler(sections[5])

    with open(BASE_DIR / 'temp' / 'parsed_response_sheet.json', "w") as file:
        file.write(json.dumps(response_sheet_content))


def main():
    create_response_sheet_json()


if __name__ == "__main__":
    main()
