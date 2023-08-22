FROM python:3.8

WORKDIR /app

COPY Live.py .
COPY games/memorygame.py .
COPY games/guessgame.py .
COPY games/currencyroulettegame.py .
COPY utils.py .
COPY score.py .
COPY mainscores.py .
COPY e2e.py .
COPY score.txt .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "mainscores.py"]

