from Functions import digit_check, range_check, clear_screen, on_your_mark_check
# random used for generates random numbers
from random import randrange
# time used for screen timeout
from time import sleep
# add_score uses for updating the user score to score.txt
from Score import add_score


def game_description(difficulty):
    description = "Welcome to Memory Game, \nI'll generate %i random numbers from 1 to 101 and show them to you " \
                  "for 0.7 seconds,\nThen, you have to guess it back. GOOD LUCK!\n" % difficulty
    return description


# generate random number from 1 to 101, and inserts it to a list, then prints it for 0.7 seconds
def generate_sequence(difficulty):
    secret_list = []
    for i in range(difficulty):
        secret_number = randrange(1, 102)
        secret_list.append(secret_number)
    print(secret_list)
    sleep(0.7)
    clear_screen()
    return secret_list


# gets guesses from user
def get_list_from_user(difficulty):
    user_list = []
    print("What do you remember?")
    for i in range(difficulty):
        current_run = i + 1
        # gets user guess and verifies whether it's a digit and also if it in range
        user_number = range_check(digit_check(input("#%i: " % current_run)), 102)
        # checks if the guess already in the list, if so, ask for different guess
        while user_number in user_list:
            print("You already guessed this number, try another one: ")
            user_number = range_check(digit_check(input("#%i: " % current_run)), 102)
        user_list.append(user_number)
    return user_list


# compares both lists and declares win or lose
def is_list_equal(secret_list, user_list, difficulty):
    secret_list.sort()
    user_list.sort()
    if user_list == secret_list:
        add_score(difficulty)
        print("YOU DID IT!!!")
        return True
    else:
        print("\nThe answer was: %s" % secret_list)
        print("Your guesses: %s" % user_list)
        print("Try your luck next time.. :( ")
        return False


# the actual game
def play(difficulty):
    clear_screen()
    print(game_description(difficulty))
    on_your_mark_check()
    clear_screen()
    secret_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    # the task ask for returning True or False according to winning or losing, so I put it into a var
    win_or_lose = is_list_equal(secret_list, user_list, difficulty)
