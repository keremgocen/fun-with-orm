FROM python:3.7-slim

RUN python -m pip install --upgrade pip

WORKDIR /src

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

ENV FLASK_ENV=development
ENV FLASK_APP=app.py

# copy all project files
COPY . .