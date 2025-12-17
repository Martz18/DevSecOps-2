FROM python:3.13.7-alpine

RUN adduser --disabled-password --gecos "" alexuser
USER alexuser

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/app.py"]