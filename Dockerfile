FROM python:3.12-alpine
LABEL authors="Марина"


# Говорим Python не создавать временные файлы (.pyc) - чтобы не захламлять контейнер
ENV PYTHONDONTWRITEBYTECODE 1

# Говорим Python сразу показывать все сообщения в консоли (без задержек)
ENV PYTHONUNBUFFERED 1

ENV TZ=Europe/Moscow

WORKDIR /app
# Устанавка зависимостей для mysqlclient
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    mariadb-dev \
    pkgconfig

COPY req.pip .

RUN pip install --upgrade pip && \
    pip install -r req.pip && \
    pip install gunicorn

COPY . .
EXPOSE 8000
