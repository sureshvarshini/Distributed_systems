FROM python:slim

RUN useradd latteboi
RUN apt update && apt install -y default-libmysqlclient-dev && apt install -y build-essential

WORKDIR /home/latterouter
COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY api api
COPY cache cache
COPY database database
COPY latterouter.py latterouter.py boot.sh ./
RUN chmod +x boot.sh
# CMD python -m flask --app latterouter runserver -h 0.0.0.0

USER latteboi
EXPOSE 5000