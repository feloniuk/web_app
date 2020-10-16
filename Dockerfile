FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /zeroten_skaner
WORKDIR /zeroten_skaner
ADD requirements.txt /zeroten_skaner/
RUN pip install -r requirements.txt
ADD . /zeroten_skaner/