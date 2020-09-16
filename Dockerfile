FROM python:3
ENV PYTHONUNBUFFERED 1
RUN skdir /zeroten_skaner
WORKDIR /zeroten_skaner
ADD requirements.txt /zeroten_skaner/
RUN pip install -r requirements.txt
ADD . /zeroten_skaner/