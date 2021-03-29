# CUSTOM ABBR USED
# PSC = Physics Single Correct
# PSN = Physics Single Not Correct
# PSL = Physics Single Left
# PHYS = Physics Single

import json
from .constants import BASE_DIR
from .generation import generate



def section_calculate_marks(section_dict, answer_dict):
    CORRECT = {}
    NOTCORRECT = {}
    LEFT = {}
    
    for key in section_dict:
        answer = answer_dict.get(key, 'D')
        question = section_dict[key]
        # 4 Cases 
        # "Not" is found in status
        if question['status'].find('Not') != -1: # Question Is Not Answered.
            question['correct_answer'] = answer
            LEFT[key] = (question)
        
        elif answer == "D": # Question has been Dropped
            question['correct_answer'] = "Question Dropped"
            CORRECT[key] = (question)
        
        elif 'or' in answer: # Multiple Correct
            answers = [ans.split() for ans in answer.split('or')]
            if question['answer_given'] in answers:
                CORRECT[key] = (question)
            else:
                NOTCORRECT[key] = (question)
                
        elif question['answer_given'] == answer: # The question is correctly attempted.
            question['correct_answer'] = answer
            CORRECT[key] = (question)
        
        elif question['answer_given'] != answer: # The question is incorrectly attempted.
            question['correct_answer'] = answer
            NOTCORRECT[key] = (question)
    
    return len(CORRECT), len(NOTCORRECT), len(LEFT), CORRECT, NOTCORRECT, LEFT

def calculate(response_dict, answer_dict):
    MARKS = 0 # Marks Counter
    QUESTIONS = {
        "PSC":{}, # +4
        "PSN":{}, # -1
        "PSL":{}, # +0
        
        "PIC":{}, # +4
        "PIN":{}, # +0
        "PIL":{}, # +0
        
        "CSC":{}, # +4
        "CSN":{}, # -1
        "CSL":{}, # +0
        
        "CIC":{}, # +4
        "CIN":{}, # +0
        "CIL":{}, # +0
        
        "MSC":{}, # +4
        "MSN":{}, # -1
        "MSL":{}, # +0
        
        "MIC":{}, # +4
        "MIN":{}, # +0
        "MIL":{}, # +0
        
        "__INF__":{}
    }
    INFO = response_dict['info']
    PHYS = response_dict['physics-single']
    CHMS = response_dict['chemistry-single']
    MTHS = response_dict['maths-single']
    PHYI = response_dict['physics-integer']
    CHMI = response_dict['chemistry-integer']
    MTHI = response_dict['maths-integer']
    # Physics Single Calc
    
    t_correct, t_incorrect, t_left = 0, 0, 0
    
    correct, incorrect, left, QUESTIONS['PSC'], QUESTIONS['PSN'], QUESTIONS['PSL'] = section_calculate_marks(PHYS, answer_dict)
    MARKS += (correct * 4)
    MARKS += (incorrect * -1)
    MARKS += (left * 0)
    t_correct += correct
    t_incorrect += incorrect
    t_left += left
    
    # Physics Integer Calc
    correct, incorrect, left, QUESTIONS['PIC'], QUESTIONS['PIN'], QUESTIONS['PIL'] = section_calculate_marks(PHYI, answer_dict)
    MARKS += (correct * 4)
    MARKS += (incorrect * 0)
    MARKS += (left * 0)
    t_correct += correct
    t_incorrect += incorrect
    t_left += left
    
    # Chemistry Single Calc
    correct, incorrect, left, QUESTIONS['CSC'], QUESTIONS['CSN'], QUESTIONS['CSL'] = section_calculate_marks(CHMS, answer_dict)
    MARKS += (correct * 4)
    MARKS += (incorrect * -1)
    MARKS += (left * 0)
    t_correct += correct
    t_incorrect += incorrect
    t_left += left
    
    # Chemistry Integer Calc
    correct, incorrect, left, QUESTIONS['CIC'], QUESTIONS['CIN'], QUESTIONS['CIL'] = section_calculate_marks(CHMI, answer_dict)
    MARKS += (correct * 4)
    MARKS += (incorrect * 0)
    MARKS += (left * 0)
    t_correct += correct
    t_incorrect += incorrect
    t_left += left
    
    # Maths Single Calc
    correct, incorrect, left, QUESTIONS['MSC'], QUESTIONS['MSN'], QUESTIONS['MSL'] = section_calculate_marks(MTHS, answer_dict)
    MARKS += (correct * 4)
    MARKS += (incorrect * -1)
    MARKS += (left * 0)
    t_correct += correct
    t_incorrect += incorrect
    t_left += left
    
    # Maths Integer Calc
    correct, incorrect, left, QUESTIONS['MIC'], QUESTIONS['MIN'], QUESTIONS['MIL'] = section_calculate_marks(MTHI, answer_dict)
    MARKS += (correct * 4)
    MARKS += (incorrect * 0)
    MARKS += (left * 0)
    t_correct += correct
    t_incorrect += incorrect
    t_left += left
    
    with open(BASE_DIR / 'temp' / 'final_results.json', 'w') as file:
        INFO['Marks'] = MARKS 
        INFO['correct'] = t_correct
        INFO['incorrect'] = t_incorrect
        INFO['left'] = t_left
        QUESTIONS['__INF__'] = INFO 
        
        file.write(json.dumps(QUESTIONS))
    generate(QUESTIONS) # Responsible for the Generation Logic
    return QUESTIONS
    
