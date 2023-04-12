FROM python:slim

RUN useradd latterouter
RUN apt update && apt install -y default-libmysqlclient-dev && apt install -y build-essential

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN chown -R latterouter:latterouter ./
USER latterouter

EXPOSE 5001