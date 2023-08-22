import random
from score import add_score
from utils import screen_cleaner, scores_file_name, bad_return_code

def generate_number(dif):
    secret_number = random.randint(1, dif)
    return secret_number

def get_guess_from_user():
    while True:
        user_choice = input('What do you think the secret number is?: ')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice >= 1 and user_choice <= 5:
                return user_choice
            else:
                print('Please choose a number between 1 and 5')
        else:
            print("can't use string")

def compare_results(secret_number, user_choice):
    if secret_number == user_choice:
        return True
    else:
        return False

def play(dif, scores_file_name, bad_return_code):
    while True:
        secret_number = generate_number(dif)
        user_choice = get_guess_from_user()
        result = compare_results(secret_number, user_choice)
        if result:
            print("Good job! You win!")
            add_score(dif, scores_file_name, bad_return_code)
        else:
            print(f'Sorry, you are lost! Secret number was {secret_number}')
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

