## Реализация сайта на Django с использованием Bootstrap 5, django-filer, Lightbox2 и Slick Slider. 
Проект представляет собой одностраничный сайт с информацией
о космическом агентстве Nasa и фотогалереей, 
управляемой через административную панель.

## Функциональность
### Главная страница 
- отображен раздел «Фотографии» со слайдером (Slick Slider).

- Полноэкранной галереей при клике на основное фото (Lightbox2).

### Административная панель Django для управления фотографиями:

- Загрузка изображений через django-filer

- Сортировка записей с помощью django-admin-sortable2

- Отображение превью картинок в списке записей

- Русскоязычные названия в админ-панели.

### Технологии
- Python 3.12

- Django 5.2

- MySQL

- Bootstrap 5

- Slick Slider 1.8.1

- Django Filer

- Django Admin Sortable2
- Lightbox2

- Easy Thumbnails (зависимость django-filer)
- CSS
- JS


## Клонирование репозитория
##### git clone https://github.com/Lavandazz/nasa.git

## Запуск приложения
##### docker-compose up --build
или
##### docker-compose build
##### docker-compose up
для новых версий
##### docker compose build
##### docker compose up
#### Для docker запуска: 
http://localhost:8000
#### Админ-панель: 
http://localhost:8000/admin/
### --- Админ создастся автоматически из заполненного .env файла. ---


## Локальный запуск (без Docker)
### Установка зависимостей
pip install -r req.pip
### .env файл
Пример .env файла в [.env_example](.env_example)
### # Создание суперпользователя
python manage.py createsuperuser
### # Запуск приложения
python manage.py runserver
