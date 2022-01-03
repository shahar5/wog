FROM python:3-alpine

WORKDIR /app

COPY requirements.txt /app/
COPY Utils.py /app/
COPY MainScores.py /app/
COPY Scores.txt /app/

RUN pip install -r /app/requirements.txt

VOLUME /app/

CMD [ "python", "MainScores.py" ]
