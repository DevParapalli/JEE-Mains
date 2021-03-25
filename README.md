# JEE-Mains

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
- `PAPR` is the paper in 4 digits (TECH for BE/BTech, PLAN for Planning, ARCH for B.Arch, PLAR for Planning and Arch)

I am working on the Mar Attempt Answer Keys.
All February Attempt Keys are available now.

### LANGUAGES INFO

```plaintext
Urdu = UDU
Assamese = ASM
Bengali = BEN
English = ENG
Gujarati = GUJ
Hindi = HIN
Kannada = KAN
Malayalam = MAL
Marathi = MAR
Odia = ODA
Punjabi = PUN
Tamil = TML
Telugu = TGU
```

## HOW-TOs

1. Download this repository using either the download option in GitHub or `git clone https://github.com/DevParapalli/JEE-Mains.git`
2. You need to have Python3.7 or greater installed. run `python -m pip install -r requirements.txt` to get the requirements.
3. Save the response sheet page as a webpage file. Rename it to `response_sheet` and place it in the `save_response_sheet_here` folder.
4. Run the program using `python main.py`.
5. Open the generated HTML file to access your results.

- In case of errors or mistakes in the data, contact me over email using the address given above.

## TO-DO

- This list is in no particular order.

- ![Progress](https://progress-bar.dev/25/) BE/BTech and B.Arch/Planning seperation. (Answer Keys is done.)
- ![Progress](https://progress-bar.dev/100/) Auto determination of Shift Code
- ![Progress](https://progress-bar.dev/60/) Answer Key Extraction/Importation (Partially, I cant extract from PDFs automatically.)
- ![Progress](https://progress-bar.dev/0/) Website Monitor (JEE Mains Result Declaration etc.)
- ![Progress](https://progress-bar.dev/65/) Auto Downloader for Response Sheet(s). (logic ready, working on implimentation)
- ![Progress](https://progress-bar.dev/90/) Automatically updating answer-keys. (Need hash verification or time checking, downloads and correction work as intended.)
- ![Progress](https://progress-bar.dev/0/) Helper Scripts to check for and correct errors. (Need to know what errors are possible.)
- ![Progress](https://progress-bar.dev/50/) A way to check multiple urls/response sheets at a time. # Educational Institutes pls contact me over email. I am sure we can work out something.
- ![Progress](https://progress-bar.dev/0/) A Graphical User Interface. (Need to finalize functionality first.)
- ![Progress](https://progress-bar.dev/100/) Response Sheet Parsing.(Completed for TECH, PLANNING, Need Example Sheets for Arch.)
- ![Progress](https://progress-bar.dev/80/) Add a HOW-TO to README.md (Expect a documentation rewrite soon.)
- ![Progress](https://progress-bar.dev/100/) `config.json` is the place to configure this program.
- ![Progress](https://progress-bar.dev/35/) Setup Scripts for specific use cases
- ![Progress](https://progress-bar.dev/0/) Rewrite program to be more optimized and faster. Will probably try to decrease parsing and iterations as much as possible. Currently parses 4 times and iterates questions approx 3 times for 1 calculation. 
