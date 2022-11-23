
FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /backend/

COPY ./requirements/requirements.txt /backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

COPY ./app /backend/app

EXPOSE 8000


CMD ["python", "server.py", "runserver", "0.0.0.0:8000"]
