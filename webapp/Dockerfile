# start with a base image
FROM python:3.7

# update pip
RUN python -m pip install --upgrade pip

# set working diretory
WORKDIR /src

# copy requirements.txt and install
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

ENV FLASK_ENV=development
ENV FLASK_APP=app.py

# copy all project files
COPY . .