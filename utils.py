import os

scores_file_name = 'scores.txt'
bad_return_code = 400

def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')