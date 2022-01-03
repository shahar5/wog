import MemoryGame
import GuessGame
import CurrencyRouletteGame
from Functions import games_menu, clear_screen, range_check, digit_check, matches_game_names, ask_for_replay


# the actual game
def load_game():
    games_menu()
    # verifies whether the chosen game is a digit and also if it in range
    game_number = range_check(digit_check(input(games_menu())), 4)
    # matches chosen game number to game name
    game_name = matches_game_names(game_number)
    # verifies whether the chosen difficulty is a digit and also if it in range
    difficulty = range_check(digit_check(input("Please choose a difficulty for %s from 1 to 5: " % game_name)), 6)
    # let's the games begin!!!
    if game_number == 1:
        MemoryGame.play(difficulty)
    elif game_number == 2:
        GuessGame.play(difficulty)
    else:
        CurrencyRouletteGame.play(difficulty)
    # first option if to play again the same game, second option is return to main menu, third is to quit the program
    answer = ask_for_replay()
    while answer == "yes_game" or answer == "y_game":
        # let's the games begin!!!
        if game_number == 1:
            MemoryGame.play(difficulty)
            answer = ask_for_replay()
        elif game_number == 2:
            GuessGame.play(difficulty)
            answer = ask_for_replay()
        else:
            CurrencyRouletteGame.play(difficulty)
            answer = ask_for_replay()
    if answer == "yes_menu" or answer == "y_menu":
        clear_screen()
        load_game()
    else:
        print("Hope you enjoyed,Thank you & Goodbye!")
