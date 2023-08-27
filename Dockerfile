FROM python:3.11.4
ENV PYTHONUNBUFFERED 1
WORKDIR /librarymanagement
ADD . /librarymanagement

COPY ./requirements.txt /librarymanagement/requirements.txt

RUN pip install -r requirements.txt

COPY . /librarymanagement