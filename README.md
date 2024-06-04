## Task from interview for Python backend

Ваша компания отправляет СМС с трекинговой ссылкой, но ссылка достаточно длинная и из-за этого СМС выходит за 70 символов (длина 1 СМС). Необходимо спроектировать сервис-«укорачиватель ссылок», чтобы сэкономить деньги компании. Интервьюер при этом выступает заказчиком со стороны бизнеса и ему можно задавать вопросы по сути задачи.

## Solution: URL shortener using Flask and Redis
- Class for writing and reading keys of database
- Flask app with post form
- Redis database get and set using redis-py

## Installation
```
python -m venv venv 
source venv/bin/activate
python main.py
```
Also be sure to have redis running
