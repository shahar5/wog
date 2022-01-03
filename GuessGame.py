from Functions import range_check, digit_check, clear_screen
# random used for generates random numbers
from random import randrange
# add_score uses for updating the user score to score.txt
from Score import add_score


def game_description(difficulty):
    clear_screen()
    description = "Welcome to Guess Game, \n" \
                  "I'll generate a number between 1-%i and you have to guess it back. GOOD LUCK!!!\n" % (difficulty + 1)
    return description


# generates random number between 1 to difficulty +1
def generate_number(difficulty):
    # difficulty +2 because it does not include the end number
    secret_number = randrange(1, difficulty + 2)
    return secret_number


# gets user guess and verifies whether it's a digit and also if it in range
def get_guess_from_user(difficulty):
    user_number = range_check(digit_check(input("Please choose a number between 1-%i: " % (difficulty + 1))), difficulty + 2)
    return user_number


# compares results and declares win or lose
def compare_results(secret_number, user_number, difficulty):
    if secret_number == user_number:
        add_score(difficulty)
        print("\nYOU WON!!!")
        return True
    else:
        print("\nMaybe you'll be luckier next time :( ")
        print("The secret number was: %i" % secret_number)
        return False


# the actual game
def play(difficulty):
    clear_screen()
    print(game_description(difficulty))
    secret_number = generate_number(difficulty)
    user_number = get_guess_from_user(difficulty)
    # the task ask for returning True or False according to winning or losing, so I put it into a var
    win_or_lose = compare_results(secret_number, user_number, difficulty)
