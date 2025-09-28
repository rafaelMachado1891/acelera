FROM python:3.12.4-slim

RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/list/*

WORKDIR /app

COPY desafio-01/ /app/

RUN sqlite3 acelera.db < desafio-01.sql

CMD [ "sqlite3", "acelera.db" ]
