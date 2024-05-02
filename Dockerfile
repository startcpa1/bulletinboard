FROM python:3

WORKDIR /bulletinboard_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
