# CRM система для банка

## Frontend

### Фронтенд выполнен на Vue3 Composition API с ипользованием Router, Pinia, PrimeVue. Реализован механиз Drag&Drop. Для Http запросов используется axios

## Backend

### Серверная часть реализована на Django с собственным API для работы с MySQL

## Инструкции

Запустить проект комплексном
```sh
docker-compose up
```

Для запуска контейтера с фронтом

```sh
cd frontend/ && docker run -v ${PWD}:/app -v /app/node_modules -p 5173:5173 --rm crm-frontend
```

MysqlDump

```sh
mysqldump -u root -h 127.0.0.1 -P 3306 -p crm-sistem > dump.sql
```