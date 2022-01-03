from Utils import SCORES_FILE_NAME
from flask import Flask


def score_server():
    app = Flask(__name__)

    @app.route('/')
    def index():
        try:
            with open(SCORES_FILE_NAME, "r") as score_file:
                content = score_file.read()
            return "<h1>The score is: </h1> <h1> %s</h1>" % content
        except Exception as e:
            return "<h1> %s </h1>" % e.args

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')


score_server()
