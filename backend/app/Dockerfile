
FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app/backend/app

COPY requirements.txt ./

RUN python -m pip install --upgrade pip

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000


CMD ["python", "server.py", "runserver", "0.0.0.0:8000"]
