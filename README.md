# World Of Games - DevOps Experts project
Python program which contains 3 games and represents the user score in a Python Flask application.
The flask application itself is a container which jenkins runs tests agains it and pushes successful builds to [this repo](https://hub.docker.com/repository/docker/ricksanchezz/wog-flask-prod).

### Games
- Currency Roulette
- Guess Game
- Memory Game

### Games description
- Currency Roulette - You'll get an amount in USD and have to guess how much is it in ILS, the number needs to be within a range accordent to the chosen difficulty
- Guess Game - A random number will be generated and you'll have to guess what it is, correct guess will be if it in the range of the chosen difficulty.
- Memory Game - The good old Memory Game, the system will generate X amount of numbers (according to the chosen difficulty), display it for 0.7 seconds and you'll have to guess what they were.


### Prerequisites
- Python
- Docker
- Jenkins

### Setup
- MainGame.py - Playing games.
- docker-run-command.txt - Pulls & runs the score dashboard (Flask app) from the repo.

### CI process
1. Developers pushes staged images to [staged repo](https://hub.docker.com/repository/docker/ricksanchezz/wog-flask-stage).
2. Jenkins pulls those images and runs selenium tests agains it to verify the Flask app is working.
3. Jenkins will push the verified images to [prod repo](https://hub.docker.com/repository/docker/ricksanchezz/wog-flask-prod).
4. Cleanup environment.

Enjoy!
