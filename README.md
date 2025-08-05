# Quizzical

Quizzical is a modular Django application for creating and taking customizable exams and quizzes.  
It features:

- **Domain-driven architecture** for clean separation of logic
- **REST API** using Django REST Framework
- **Frontend UI** with Tailwind CSS via `django-tailwind`
- **SQLite** for development database (default)

---

## 🛠️ Prerequisites

Before starting, ensure the following tools are installed on your system:

### Required System Tools

- Python 3.10+ — https://www.python.org/downloads/
- pip — Installed with Python
- Node.js (v16 or later) — https://nodejs.org/
- npm (comes with Node.js)
- Git — https://git-scm.com/

---

## 🚀 Quick Start: Full Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/quizzical.git
cd quizzical
```

### 2. Install Python Dependencies

```bash
pip install django djangorestframework django-tailwind
```

### 3. Create Required Django Apps (If Not Already Created)

```bash
python manage.py startapp domain  # if not already created
python manage.py startapp api     # if not already created
python manage.py startapp ui      # if not already created
```

### 4. Register Django Apps

In `quizzical/settings.py`, ensure the following apps are listed in `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'tailwind',
    'theme',
    'domain',
    'api',
    'ui',
]
```

### 5. Configure Tailwind CSS

```bash
python manage.py tailwind init theme
cd theme && npm install && cd ..
python manage.py tailwind build
```

Add to `settings.py`:

```python
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ['127.0.0.1']
```

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. (Optional) Create a Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000

---

## 🔐 Custom User Model

Make sure this is set in `settings.py`:

```python
AUTH_USER_MODEL = 'domain.User'
```

---

## 📡 API Access

Add this to `quizzical/urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path("api/", include("api.urls")),
]
```

---

## ✅ Setup Summary (All Commands)

```bash
git clone https://github.com/your-org/quizzical.git
cd quizzical

pip install django djangorestframework django-tailwind

python manage.py startapp domain  # if not already created
python manage.py startapp api     # if not already created
python manage.py startapp ui      # if not already created

python manage.py tailwind init theme
cd theme && npm install && cd ..

python manage.py tailwind build

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # optional

python manage.py runserver
```
