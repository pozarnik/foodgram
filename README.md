# Foodgram

***Foodgram - сайт для размещения кулинарных рецептов***

## Возможности проекта Foodgram

- Реализована регистрация пользователей через djoser
- Вход на сайт осуществляется с помощью электронной почты и пароля
- Публикация рецептов, с добавлением необходимых ингридиентов и времени приготовления
- Поиск по ингридиентам при создании рецепта
- Возможность задать теги для рецептов
- Фильтрация рецептов по тегам
- Подписка на авторов рецептов, добавление рецептов в избранное
- Добавление рецептов в корзину покупок и скачивание их списка продуктов в txt

## Особенности настройки Docker

- Проект запускается в четырех контейнерах: nginx, PostgreSQL и Django
- Обновление образа проекта в Docker Hub

## Технологии

- Python 3.9
- Django 4.0.4
- Django REST framework 3.13.1
- PostgreSQL 14.3
- Gunicorn 20.1.0
- nginx 1.22.0
- React

## Установка и запуск проекта

...

В папке infra создайте файл .env и добавьте в него переменные с вашими данными:

```
SECRET_KEY=           # ключ для генерации хэша Django
DEBUG=                # значение Debug
ALLOWED_HOSTS=[]      # разрешенные хосты
DB_ENGINE=            # укажите используемую БД
DB_NAME=              # имя базы данных
POSTGRES_USER=        # логин для подключения к БД
POSTGRES_PASSWORD=    # пароль для подключения к БД (установите свой)
DB_HOST=              # название сервиса (контейнера) БД
DB_PORT=              # порт для подключения к БД 
```

Запустите docker-compose

```sh
sudo docker-compose up -d --build
```

Cоздайте суперпользователя

```sh
sudo docker-compose exec web python manage.py createsuperuser
```

Остановка docker-compose и удаление всех созданных Docker папок и томов проекта

```sh
sudo docker-compose down -v
```

## Документации проекта Foodgram

При запущенном проекте откройте ссылку в браузере:

```sh
http://localhost/api/docs/redoc.html
```

## Мои профили

- [GitHub](https://github.com/pozarnik/)
- [LinkedIn](https://www.linkedin.com/in/alekseyevich-ivan/)

## License

MIT



