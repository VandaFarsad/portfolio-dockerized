FROM python:3.11-slim

WORKDIR /code

# copy our nginx configuration to overwrite nginx defaults
COPY ./conf/nginx.conf /etc/nginx/conf.d/default.conf

# install dependencies
COPY requirements requirements
RUN pip install --no-cache-dir --upgrade -r requirements/production.txt
RUN apt-get update && apt-get install -y libexempi8 gcc make libmariadb-dev nginx

# copy the scripts to the folder

COPY . .

EXPOSE 8000

ENTRYPOINT ["bash", "/code/docker-entrypoint.sh"]