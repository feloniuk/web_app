FROM python:3.8
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app/src
CMD gunicorn app.wsgi:application --bind 0.0.0.0:8000