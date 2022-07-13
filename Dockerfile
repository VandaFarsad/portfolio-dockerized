FROM python:3.10-slim

WORKDIR /code

# install dependencies

COPY requirements requirements
RUN pip install --no-cache-dir --upgrade -r requirements/production.txt
RUN apt-get update && apt-get install -y libexempi8 gcc make libmariadb-dev git

# copy the scripts to the folder

COPY . .

EXPOSE 8000

ENTRYPOINT ["bash", "/code/docker-entrypoint.sh"]