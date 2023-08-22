import random
import requests
from score import add_score
from utils import screen_cleaner, scores_file_name, bad_return_code

api_key = "7419ef3150c24dcfa5bb37678bb6b866"
url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"

def get_money_interval(dif):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        money_rate = data['rates']['ILS']
    print(f'USD rate: {money_rate}')
    sum_dol = random.randint(1, 100)
    print(f'amount of USD: {sum_dol}')
    usd_to_ils = sum_dol*money_rate
    money_interval = (usd_to_ils-(5-dif), usd_to_ils+(5-dif))
    return money_interval

def get_guess_from_user():
    while True:
        guess_from_user = input('How much ILS is it: ')
        if guess_from_user.isdigit():
            return int(guess_from_user)
        else:
            print('Invalid input.Only numbers')

def play(dif, scores_file_name, bad_return_code):
    while True:
        money_interval = get_money_interval(dif)
        guess_from_user = get_guess_from_user()
        if money_interval[0] <= guess_from_user <= money_interval[1]:
            print("Good job! Your answer is correct")
            add_score(dif, scores_file_name, bad_return_code)
        else:
            print("Sorry, it's incorrect answer")
        play_again = input('Want to play again? yes or no: ')
        if play_again == "no":
            next_game = input('Want to choose another game? yes or no: ')
            if next_game == "yes":
                from Live import load_game
                load_game()
            else:
                print("See you")
            break
        print("Let's go")
