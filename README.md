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
cd frontend/
```

```sh
docker run -v ${PWD}:/app -v /app/node_modules -p 5173:5173 --rm vue-test
```