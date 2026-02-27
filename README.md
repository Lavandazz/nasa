## Реализация сайта на Django с использованием Bootstrap 5, django-filer, Lightbox2 и Slick Slider. 
Проект представляет собой одностраничный сайт с информацией
о космическом агентстве Nasa и фотогалереей, 
управляемой через административную панель.

## Функциональность
### Главная страница 
- отображен раздел «Фотографии» 
с синхронизированным слайдером (Slick Slider).

- Полноэкранной галереей при клике на основное фото (Lightbox2).

### Административная панель Django для управления фотографиями:

- Загрузка изображений через django-filer

- Drag-and-drop сортировка записей с помощью django-admin-sortable2

- Отображение превью картинок в списке записей

- Русскоязычные названия в админ-панеле.

### Технологии
- Python 3.12

- Django 5.2

- MySQL

- Bootstrap 5

- Slick Slider 1.8.1

- Django Filer

- Django Admin Sortable2

- Easy Thumbnails (зависимость django-filer)
- CSS
- JS


## Клонируйте репозиторий
##### git clone https://github.com/Lavandazz/nasa.git

## Запустите приложение
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

## Локальный запуск (без Docker)

### Установите зависимости
### Создайте .env файл
Пример .env файла в [.env_example](.env_example)
### # Создайте суперпользователя
python manage.py createsuperuser
### # Запустите приложение
python manage.py runserver
