# 📱 PhoneShop — Django E-commerce Project

Небольшой интернет-магазин телефонов, реализованный на Django.  
Проект демонстрирует базовую backend-логику, работу с БД, корзиной и UI.

---

## 🚀 Функционал

- 🔍 Поиск товаров
- 📂 Фильтр по категориям
- 🛒 Корзина (добавление / удаление / изменение количества)
- 📦 Просмотр товаров
- 🔐 Авторизация пользователей
- 🎨 UI на Bootstrap
- 💣 Кастомная 404 страница с эффектами

---

## 🧠 Стек технологий

- Python 3.12
- Django 6
- SQLite
- HTML / CSS / Bootstrap 5
- JavaScript (анимации, эффекты)

---

## 📂 Структура проекта
apps/
├── products/ # товары и категории
├── cart/ # логика корзины
└── users/ # авторизация

templates/
static/
media/



---

## ⚙️ Установка и запуск

```bash
git clone https://github.com/your-username/phone-shop.git
cd phone-shop

python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt

🗄 Миграции
python manage.py makemigrations
python manage.py migrate

👤 Создание админа
python manage.py createsuperuser

▶️ Запуск
python manage.py runserver

📸 Медиа

Для корректной работы изображений:

DEBUG = True

📌 Примечание

Проект учебный, но приближен к реальной структуре backend-приложений.


## 🚧 Развитие проекта
- Добавление отзывов и рейтингов
- Реализация платежной системы
- Улучшение UI/UX
- Оптимизация производительности

💼 Автор

Xoja — начинающий backend разработчик


