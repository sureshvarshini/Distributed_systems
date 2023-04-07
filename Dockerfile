FROM python:slim

RUN useradd latteboi

WORKDIR /home/latterouter
COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY api api
COPY Cache cache
COPY database database
COPY latterouter.py latterouter.py boot.sh ./
RUN chmod +x boot.sh 

USER latteboi
EXPOSE 5000