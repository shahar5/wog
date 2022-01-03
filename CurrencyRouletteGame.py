from Functions import range_check, digit_check, clear_screen
# requests used for api requests
import requests
# json used for converting the api request into dictionary
import json
# random used for generates random numbers
from random import randrange
# add_score uses for updating the user score to score.txt
from Score import add_score


def game_description(difficulty):
    clear_screen()
    description = "Welcome to Currency Roulette Game, \n" \
                  "I'll give you an amount in USD and you have to guess how much is it in ILS.\n" \
                  "Your guess has to be in the range of +-%i from the number. GOOD LUCK!!!\n" % difficulty
    return description


###
# gets the USD-ILS current rate, generate random number between 1 to 100,
# creates interval according to the chosen difficulty of +-difficulty from the generated number.
# for example for number 50 and difficulty 1, the interval will be 45-55.
###
def get_money_interval(difficulty):
    # gets all currencies from a base of USD
    response = requests.get("https://freecurrencyapi.net/api/v2/latest?apikey=c14e88e0-2dfd-11ec-a32b-c53f7a44419d"
                            "&base_currency=USD")
    # inserts the whole response into a dictionary
    response_dict = json.loads(response.text)
    # takes only the currency rates from the dictionary above and create a new dictionary with rates only
    currencies_rates_dict = response_dict.get("data")
    # finds from all rates the USD-ILS rate and puts as a var
    usd_to_ils = currencies_rates_dict.get("ILS")
    # # generates random number from 1 to 100
    secret_number = randrange(1, 101)
    # converts the random number into ILS rate
    ils_secret_number = secret_number * usd_to_ils
    ils_secret_number = int(ils_secret_number)
    # creates interval according the difficulty: -+5 for difficulty 1, -+1 for difficulty 5
    range_beginning = (ils_secret_number - (5 - difficulty + 1))
    range_ending = (ils_secret_number + (5 - difficulty + 1))
    return secret_number, range_beginning, range_ending, ils_secret_number


def get_guess_from_user(secret_number):
    # verifies whether the chosen guess is a digit and also if it in range
    user_guess = range_check(digit_check(input("%i$ to ILS: " % secret_number)), 401)
    return user_guess


# compares the user guess to the interval and declares win or lose
def validate_guess(user_guess, range_beginning, range_ending, difficulty, ils_secret_number):
    if user_guess in range(range_beginning, range_ending + 1):
        add_score(difficulty)
        print("\nYOU WON!!!")
        print("The accurate answer is: %i" % ils_secret_number)
        return True
    else:
        print("\nThe answer was: %i" % ils_secret_number)
        print("Try your luck next time.. :( ")
        return False


# the actual game
def play(difficulty):
    clear_screen()
    print(game_description(difficulty))
    money_interval_function_returns = get_money_interval(difficulty)
    secret_number = money_interval_function_returns[0]
    range_beginning = money_interval_function_returns[1]
    range_ending = money_interval_function_returns[2]
    ils_secret_number = money_interval_function_returns[3]
    user_guess = get_guess_from_user(secret_number)
    # the task ask for returning True or False according to winning or losing, so I put it into a var
    win_or_lose = validate_guess(user_guess, range_beginning, range_ending, difficulty, ils_secret_number)
