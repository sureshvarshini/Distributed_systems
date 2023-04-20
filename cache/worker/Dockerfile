FROM python:slim

WORKDIR /cache/worker

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . . 