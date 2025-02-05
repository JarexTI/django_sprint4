# Социальная сеть "Блогикум" (RU)

Описание проекта
---
Проект представляет собой блог-платформу на Django. В нем реализованы ключевые функции: создание и редактирование публикаций, система комментариев, работа с пользователями, пагинация, а также настройка кастомных страниц для ошибок и отправка электронных писем.

Основные задачи
---
✔️ Создание моделей для постов, категорий и пользователей  
✔️ Реализация системы комментариев и профилей пользователей  
✔️ Подключение кастомных страниц ошибок  
✔️ Настройка системы пагинации и добавление изображений к публикациям  
✔️ Реализация функционала отправки email-уведомлений

Стек технологий
---
- Python 3.9
- Django 3.2
- HTML, CSS

Установка проекта из репозитория (Windows)
---
1. Клонировать репозиторий:
```bash
git clone git@github.com:JarexTI/django_sprint4.git
```
2. Создать и активировать виртуальное окружение:
```bash
python -m venv venv

source venv/Scripts/activate
```
3. Установить зависимости из файла `requirements.txt`:
```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```
4. Выполнить миграции
```
python blogicum/manage.py migrate
```
5. Загрузить фикстуры DB
```
python blogicum/manage.py loaddata blogicum/db.json
```
6. Создать суперпользователя
```
python blogicum/manage.py createsuperuser
```
7. Запустить проект:
```bash
python blogicum/manage.py runserver
```
8. Переходим на сервер разработки:
```bash
http://127.0.0.1:8000/
```
<br>

# Social Network "Blogicum" (EN)

Project Description
---
This project is a blog platform built with Django. It implements key features such as creating and editing posts, a comment system, user management, pagination, as well as custom error pages and email notifications.

Key Tasks
---
✔️ Creating models for posts, categories, and users  
✔️ Implementing the comment system and user profiles  
✔️ Integrating custom error pages  
✔️ Setting up pagination and adding images to posts  
✔️ Implementing email notification functionality

Technology Stack
---
- Python 3.9
- Django 3.2
- HTML, CSS

Setting Up the Project from Repository (Windows)
---
1. Clone the repository:

```bash
git clone git@github.com:JarexTI/django_sprint4.git
```

2. Create and activate the virtual environment:

```bash
python -m venv venv

source venv/Scripts/activate
```

3. Install dependencies from `requirements.txt`:

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```

4. Run migrations:

```bash
python blogicum/manage.py migrate
```

5. Load DB fixtures:

```bash
python blogicum/manage.py loaddata blogicum/db.json
```

6. Create a superuser:

```bash
python blogicum/manage.py createsuperuser
```

7. Run the project:

```bash
python blogicum/manage.py runserver
```

8. Go to the development server:

```bash
http://127.0.0.1:8000/
```
