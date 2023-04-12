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

CMD ["python", "-m", "flask", "--app", "latterouter", "run", "-h", "0.0.0.0", "--debug"]

EXPOSE 5000