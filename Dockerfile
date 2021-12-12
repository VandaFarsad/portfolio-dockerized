FROM python:3.10.0-slim

WORKDIR /code

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y libexempi8\
    gcc make libmariadb-dev git

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000
