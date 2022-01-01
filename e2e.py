# imports
# -----------
from selenium import webdriver
import os

# vars setups
# ------------
my_driver = webdriver.Chrome(executable_path=os.environ.get("CHROME_DRIVER"))
website_url = "http://localhost:8777"


# functions
# -----------
# checks whether the score is a number & if in the range of 0-1000
def score_check(score):
    if score.isdigit():
        score = int(score)
        if score in range(score, 1001):
            return True
    else:
        return False

# get the score from flask
def test_scores_service():
    my_driver.get(website_url)
    score = my_driver.find_element_by_xpath("/html/body/h1[2]").text
    return score_check(score)


# checks the flask server and return o or 1 accordingly
def main_function():
    result = test_scores_service()
    if result:
        result = 0
    else:
        result = 1
    print(result)
    return result


# main
# ----------
main_function()
