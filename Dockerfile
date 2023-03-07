FROM python:3.11-buster

ENV PROJECT_DIR /srv/apps

RUN apt-get update && apt-get upgrade -y \
    && apt install -y sudo nginx unzip less gettext-base \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install supervisor pipenv

WORKDIR ${PROEJCT_DIR}
COPY . .

RUN rm -rf /etc/nginx/nginx.conf \
    && rm -rf /etc/nginx/sites-enabled/* \
    && mv ${PROEJCT_DIR}/docker/nginx/nginx.conf /etc/nginx/nginx.conf

RUN PIP_NO_CACHE_DIR=true pipenv install --system --deploy