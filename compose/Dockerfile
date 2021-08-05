FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
RUN mkdir /static
WORKDIR /app
COPY requirements.txt /app/

RUN pip install gunicorn
RUN pip install -r requirements.txt
COPY . /app/
CMD python manage.py collectstatic
CMD gunicorn -b 0.0.0.0:80 miproyecto.wsgi:application
