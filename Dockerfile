#FROM ubuntu:latest
FROM python:2.7
#----------------------------
# REFERENCIAS
# https://gitlab.com/patkennedy79/flask_recipe_app
# https://hub.docker.com/_/python/
# https://hub.docker.com/r/hjaf23/cx_oracle/~/dockerfile/
# https://hub.docker.com/r/collinestes/docker-node-oracle/builds/bzjwjwk7zdhnmqueqxvqcna/
# https://www.youtube.com/watch?v=6opltZu4ABw
#----------------------------
MAINTAINER GUSTAVO S. F. MOLLERI "GUSTAVO.MOLLERI@ANA.GOV.BR"
RUN apt-get update -y
#RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app/web
RUN pip install -r requirements.txt

#ENTRYPOINT ["python"]
#CMD ["app.py"]