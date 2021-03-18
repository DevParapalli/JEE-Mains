# NOTES

## MISC

### Sorting Algorithm

FOR EACH SECTION:
    PATH: `class:section-cntnr`
    LABEL -> `class:section-cntnr` -> `class:section-lbl` >> TEXT 
    FOR EACH QUESTION:
        PATH: `class:menu-tbl` -> `tag:tbody` ->  `tag:tr[0]` -> `tag:td[1]` >> TEXT
        Take the text and compare to :-
            `SA` for INTEGER
            `MCQ` for SINGLE CHOICE

### PARSING

INFO PANEL:
    PATH -> `class:main-info-pnl` -> `tag:table` -> FOR EACH `tag:tr`
        KEY: `tag:td[0]`
        VALUE: `tag:td[1]`

PARSING NEEDS `KNOWN QUESTION TYPE`

QUESTION ID FOR ALL:
    PATH: `class:menu-tbl` -> `tag:tbody` ->  `tag:tr[1]` -> `tag:td[1]` >> TEXT 

QUESTION STATUS FOR INTEGER:
    PATH: `class:menu-tbl` -> `tag:tbody` ->  `tag:tr[-1]` -> `tag:td[1]` >> TEXT

QUESTION STATUS FOR MCQ:
    PATH: `class:menu-tbl` -> `tag:tbody` ->  `tag:tr[-2]` -> `tag:td[1]` >> TEXT

CHOSEN OPTION FOR MCQ:
    PATH: `class:menu-tbl` -> `tag:tbody` ->  `tag:tr[-1]` -> `tag:td[1]` >> TEXT

OPTIONS FOR MCQ:
    A: `class:menu-tbl` -> `tag:tbody` ->  `tag:tr[2]` -> `tag:td[1]` >> TEXT
    B: `class:menu-tbl` -> `tag:tbody` ->  `tag:tr[3]` -> `tag:td[1]` >> TEXT
    C: `class:menu-tbl` -> `tag:tbody` ->  `tag:tr[4]` -> `tag:td[1]` >> TEXT
    D: `class:menu-tbl` -> `tag:tbody` ->  `tag:tr[5]` -> `tag:td[1]` >> TEXT

ANSWER FOR SA:
    PATH:  `class:questionRowTbl` -> `tag:tbody` ->  `tag:tr[-1]` -> `tag:td[1]` >> TEXT 
    # IS EITHER -- or integer value.
### MISC NOTES

#### We save the files in their specified folder so we can reuse if needed.

