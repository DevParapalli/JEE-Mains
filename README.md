# JEE-Mains

## NOTICE: If you have attempted JEE Mains in the current session [MARCH], Please save the correction submission page(Right Click -> Save As) and send the file to me over on email: [devparapalli@gmail.com](mailto:devparapalli@gmail.com). I can convert them into answer keys for use in this program

## WIP Notice

- This repository is a work-in-progress, the content on this repo can change very frequently. Make sure to keep up with changes on this repository.

## Introduction

1. This repository provides scripts to aid in the procedure of JEE Mains
2. Over the course of due time, Other Contributors and I will add features to this program

## ShiftCode Explanation

The shift code describes what partial answer key to download.
The format is `YYYY-MM-DD-S-LNG`.

- `YYYY` is the year in 4 digits (1995)
- `MM` is the month in 2 digits (07 for July)
- `DD` is the day in 2 digits (07)
- `S` is the shift in 1 digit (M for Morning, E for evening.)
- `LNG` is the language in 3 digits (ENG for english)

## HOW-TOs

0. Requirements: Python, run `python -m pip install -r requirements.txt`
1. Download this repository using either the download option in GitHub or `git clone https://github.com/DevParapalli/JEE-Mains.git`
2. Save the response sheet page as a webpage file. Rename it to `response_sheet` and place it in the `response_sheet` folder.
3. Make a copy of the `example_config` and rename it to `config`
4. Edit the config to correctly add your shift code.
5. Run the program using `python main.py`

## TO-DO

- This list is in no particular order.

- [x] Main Program
- [ ] Answer Key Extraction/Importation
- [ ] Website Monitor (JEE Mains Result Declaration etc.)
- [x] Auto Downloader for Response Sheet(s).
- [x] Automatically updating answer-keys.
- [ ] Helper Scripts to check for and correct errors.
- [ ] A Graphical User Interface.
- [ ] Add a setup script for windows and linux users. (BASH/PowerShellSpecific.)
- [ ] Add a fallback parser (html.parser) incase the main (lxml) fails.
- [x] Add a HOW-TO to README.md
- [x] Create a example config.json with some `??prefilled values??`
