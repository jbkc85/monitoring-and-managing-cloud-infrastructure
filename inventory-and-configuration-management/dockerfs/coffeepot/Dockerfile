FROM python:3.11.2-buster

WORKDIR /app

COPY . /app
RUN pip3 install -r /app/requirements.txt

CMD [ "python3", "/app/server.py" ]
