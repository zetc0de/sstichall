FROM python:2
MAINTAINER zetc0de "zetc0de.id@gmail.com"

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
CMD [ "python", "sstichall.py" ]