import random


def game():
    score = random.randint(1, 100)
    return score


with open("hiscore.txt", "r") as f:
    previous_score = int(f.read())
    current_score = game()
    if previous_score < current_score:
        with open("hiscore.txt", "w") as f:
            f.write(str(current_score))
            print("High Score Stored in file named --> [hiscore.txt]")
