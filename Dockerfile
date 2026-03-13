FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN adduser --disabled-password appuser
USER appuser

EXPOSE 8080

CMD ["honcho","start"]
