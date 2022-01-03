from Functions import wog_logo, welcome, input_name
from Live import load_game
from time import sleep

print(wog_logo())
sleep(2)
print(welcome(input_name()))
load_game()
