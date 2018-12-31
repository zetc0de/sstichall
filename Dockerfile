FROM ubuntu:16.04
MAINTAINER zetc0de "zetc0de.id@gmail.com"
RUN apt-get update -y 
RUN apt-get install -y python-pip python-dev build-essential nginx 
VOLUME sstichall /app 
WORKDIR /app
# COPY .requirements.txt /app/requirements.txt
# COPY ./sstichall /app
RUN pip install -r requirements.txt
ENV FLASK_APP sstichall.py


CMD ["python", "-m", "flask", "run", -"-host=0.0.0.0"]