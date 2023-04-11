FROM python:slim

RUN useradd latterouter
RUN apt update && apt install -y default-libmysqlclient-dev && apt install -y build-essential

WORKDIR /home/latterouter
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY api api
COPY cache cache
COPY database database
COPY latterouter.py latterouter.py
COPY . /home/latterouter

ENV FLASK_APP latterouter.py

RUN chown -R latterouter:latterouter ./
USER latterouter

# CMD python -m flask --app latterouter runserver -h 0.0.0.0
# CMD ["python", "-m", "flask", "--app", "latterouter", "run"]

EXPOSE 5000