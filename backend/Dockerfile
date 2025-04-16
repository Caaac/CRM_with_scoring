FROM python:3.12-alpine

WORKDIR /usr/src/app

COPY . .

RUN apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    linux-headers

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000