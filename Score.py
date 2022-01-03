from Utils import SCORES_FILE_NAME
import os.path


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    if os.path.isfile(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, "r+") as file:
            content = int(file.read()) + points_of_winning
            file.seek(0)
            file.truncate()
            file.write(str(content))
    else:
        with open(SCORES_FILE_NAME, "w") as file:
            file.write(str(points_of_winning))
