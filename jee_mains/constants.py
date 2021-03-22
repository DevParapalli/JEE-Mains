import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

with open(BASE_DIR / 'config.json') as file:
    CONFIG = json.loads(file.read())

NOTICE = """ 
+--------------------------------------------------+
| Copyright (c) 2021 Dev Parapalli                 |
|                                                  |
| This software is currently under-development.    |
| The author makes no guarantee of the usability or| 
| functionality of the software.                   |
| THE SOFTWARE IS PROVIDED "AS IS", WITHOUT        |
| WARRANTY OF ANY KIND.                            |
| Check LICENCE for more info.                     |
+--------------------------------------------------+
"""

RESULT = """
[INFO]
    NAME:               {name}
    APPLICATION NUMBER: {admn}
    ROLL NUMBER:        {roll}
    TEST DATE:          {tdte}
    TEST TIME:          {ttim}
    SUBJECT:            {subj}
    MARKS:              {mark}
    SHIFT CODE:         {shft}
"""
RESULT_TEMPLATE = """

"""