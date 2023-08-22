def add_score(dif, scores_file_name, bad_return_code):
    points_of_winning = (dif * 3) + 5
    try:
        with open('Scores.txt', 'r') as file:
            my_score = int(file.read())
    except FileNotFoundError:
        user_score = 0
    user_score += points_of_winning
    with open('score.txt', 'w') as file:
        file.write(str(user_score))
