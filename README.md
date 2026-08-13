# 📚 BookStore

A simple Django-based bookstore web application that demonstrates CRUD (Create, Read, Update, Delete) operations for managing books.

## 🚀 Features

- Add new books
- View all books
- Edit existing books
- Delete books
- Store book details using SQLite
- Django Admin interface for managing data
- Basic responsive styling with CSS

## 🛠️ Technologies Used

- Python
- Django
- SQLite
- HTML5
- CSS3
- Git & GitHub

## 📂 Project Structure

```text
BookStore/
│
├── Books/
│   ├── migrations/
│   ├── static/
│   │   └── Books/
│   │       └── style.css
│   ├── templates/
│   │   └── Books/
│   │       ├── home.html
│   │       └── edit_book.html
│   ├── admin.py
│   ├── models.py
│   └── views.py
│
├── Bookstore/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── .gitignore
