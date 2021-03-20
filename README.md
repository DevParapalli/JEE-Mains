# JEE-Mains

## NOTICE: If you have attempted JEE Mains in the current session [MARCH], Please save the correction submission page(Right Click -> Save As) and send the file and your shift to me over on email: [devparapalli@gmail.com](mailto:devparapalli@gmail.com). I can convert them into answer keys for use in this program

## WIP Notice

- This repository is a work-in-progress, the content on this repo can change very frequently. Make sure to keep up with changes on this repository.

## Introduction

1. This repository provides scripts to aid in the procedure of JEE Mains
2. Over the course of due time, Other Contributors and I will add features to this program

## CONFIG EXPLANATION

The config file contains parameters that alter the functionality of the program.

- cache mode is the way that the answer keys are fetched.
  - `online-only` fetches the answer_key every time.
  - `normal` fetches the answer key if it doesn't exist on your pc. Else uses the one already present.
  - `offline-only` only uses the answer keys saved on your pc. Raises an Exception if it doesn't exist.

- response_sheet_url contains the url to your response sheet. It usually begins with `https://cdnX.digitalm.com` etc. 
- DEBUG Flag can be set to true or false depending on the level of trouble shooting you maybe doing. Default is false.

## ShiftCode Explanation

The shift code describes what partial answer key to download.
The format is `YYYY-MM-DD-S-LNG-PAPR`.

- `YYYY` is the year in 4 digits (1995)
- `MM` is the month in 2 digits (07 for July)
- `DD` is the day in 2 digits (07)
- `S` is the shift in 1 digit (M for Morning, E for evening.)
- `LNG` is the language in 3 digits (ENG for english)
- `PAPR` is the paper in 4 digits (TECH for BE/BTech, PLAN for Planning/Arch)

Note: FOR FEB ATTEMPT USE `2021-02-BE-BTECH-MASTER` as shift code. # Working on other papers too
This is ideally an exception. The other answer keys will follow the above rule.

## HOW-TOs

1. Download this repository using either the download option in GitHub or `git clone https://github.com/DevParapalli/JEE-Mains.git`
2. You need to have Python3.7 or greater installed. run `python -m pip install -r requirements.txt` to get the requirements.
3. Save the response sheet page as a webpage file. Rename it to `response_sheet` and place it in the `save_response_sheet_here` folder.
4. Make a copy of the `example_config` and rename it to `config`
5. Edit the `config` file to correctly add your shift code. # Will work on automating this soon.
6. Run the program using `python main.py`

- In case of errors or mistakes in the data, contact me over email using the address given above.

## TO-DO

- This list is in no particular order.

- [ ] BE/BTech and B.Arch/Planning seperation.
- [ ] Auto determination of Shift Code
- [ ] Answer Key Extraction/Importation
- [ ] Website Monitor (JEE Mains Result Declaration etc.)
- [x] Auto Downloader for Response Sheet(s).
- [x] Automatically updating answer-keys.
- [ ] Helper Scripts to check for and correct errors.
- [ ] A way to check multiple urls/response sheets at a time. # Educational Institutes pls contact me over email.
- [ ] A Graphical User Interface.
- [ ] Add a setup script for windows and linux users. (BASH/PowerShellSpecific.)
- [x] Add a fallback parser (html.parser) incase the main (lxml) fails. (changed to html5lib)
- [x] Add a HOW-TO to README.md
- [x] Create a example config.json with some `??prefilled values??`
- [ ] Create a WebApp for the results, paste your url and get teh results in about 5 seconds (very late game goal)
