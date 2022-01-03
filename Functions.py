# system name used for clear the screen
from os import system, name


# game logo and screen timeout for 2 seconds
def wog_logo():
    clear_screen()
    logo = "\n\n\n\n                             ##           ##    #####      ######## \n"\
           "                             ##           ##   #######    ######### \n"\
           "                             ###         ###  ##     ##  ###        \n"\
           "                             ###         ###  ##     ##  ##         \n"\
           "                              ###       ###   ##     ##  ##   ##### \n"\
           "                              ###   #   ###   ##     ##  ##   ##### \n"\
           "                               ### ### ###    ##     ##  ##      ## \n"\
           "                               ### ### ###    ##     ##  ##      ## \n"\
           "                                #########     ##     ##  ###    ##  \n"\
           "                                 ### ###       #######    #######   \n"\
           "                                  ## ##         #####      #####    \n"
    return logo


# gets the player name for the welcome message, player name should only contain alphabet letters
def input_name():
    clear_screen()
    player_name = input("Enter your name: ")
    while not player_name.isalpha():
        player_name = input("Name can only contains alphabet letters, try again: ")
    return player_name


# clear screen to simulate a real game
def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


# prints the welcome message with the player's name
def welcome(player_name):
    clear_screen()
    welcome_message = "\nHello %s, and welcome to the World of Games (WoG). " \
                      "Here you can find many cool games to play.\n" % player_name
    return welcome_message


# verifies whether an input is a number or not and keep asking for a number
def digit_check(num):
    while not num.isdigit():
        num = input("Wrong character, please enter a number: ")
    num = int(num)
    return num


# verifies whether the input number from above is in range or not and keep asking for a number in range
def range_check(choice, some_range):
    while choice not in range(1, some_range):
        choice = digit_check(input("Wrong number, try again: "))
    return choice


# put it as a function for better visibility
def games_menu():
    menu = "Please choose a game to play:\n" \
        "1. Memory Game - a sequence of numbers will appear for 0.7 second " \
        "and you have to guess it back\n" \
        "2. Guess Game - guess a number and see if you chose like the computer\n" \
        "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n " \
        "Game: "
    return menu


def matches_game_names(game_number):
    # matches chosen game number to game name
    if game_number == 1:
        game_name = "Memory game"
    elif game_number == 2:
        game_name = "Guess Game"
    else:
        game_name = "Currency Roulette"
    return game_name


def on_your_mark_check():
    answer = input("ARE YOU READY?! (Y/N)")
    answer = answer.lower()
    answer = yes_no_check(answer)
    while answer == "n" or answer == "no":
        answer = input("ARE YOU READY?! (Y/N)")
        answer = answer.lower()
        answer = yes_no_check(answer)
    return answer


def yes_no_check(answer):
    while answer != "y" and answer != "yes" and answer != "n" and answer != "no":
        answer = input("Please enter yes or no, try again: ")
        answer = answer.lower()
    return answer


def ask_for_replay():
    answer = input("\nDo you want to play again? (Y/N)")
    answer = answer.lower()
    answer = yes_no_check(answer)
    if answer == "n" or answer == "no":
        answer = input("\nDo you want to return to main menu? (Y/N)")
        answer = answer.lower()
        answer = yes_no_check(answer)
        if answer == "n" or answer == "no":
            return answer
        else:
            return answer + "_menu"
    else:
        return answer + "_game"


def score_check(score):
    if score.isdigit():
        score = int(score)
        if score in range(score, 1001):
            return True
    else:
        return False
