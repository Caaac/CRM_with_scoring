# CRM система для банка

## Frontend

### Фронтенд выполнен на Vue3 Composition API с ипользованием Router, Pinia, PrimeVue. Реализован механиз Drag&Drop. Для Http запросов используется axios

### Реализован класс-обертка `RestService` для работы с REST и отправки запросов пакетами

## Backend

### Серверная часть реализована на Django с собственным API для работы с MySQL

### Реализована авторизация по JWT токену 

## Инструкции



Запустить проект комплексном
```sh
docker-compose -f docker-compose.dev.yml up --build
```

Для запуска контейтера с фронтом

```sh
cd frontend/ && docker run -v ${PWD}:/app -v /app/node_modules -p 5173:5173 --rm crm-frontend
```

MysqlDump

```sh
mysqldump -u root -h 127.0.0.1 -P 3306 -p crm-sistem > dump.sql
```