FROM ubuntu:latest
MAINTAINER GUSTAVO S. F. MOLLERI "GUSTAVO.MOLLERI@ANA.GOV.BR"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app/web
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]