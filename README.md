# Django Tutorial

This project is based on the [W3Schools Django tutorial](https://www.w3schools.com/django/) and demonstrates how to create web applications using Django.

## Getting Started

### 1. Create and Activate a Virtual Environment

```bash
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
# Windows
myenv\Scripts\activate.bat

# Unix/MacOS
source myenv/bin/activate
```

### 2. Install Django

```bash
pip install django
```

### 3. Create a Django Project

```bash
django-admin startproject myproject
cd myproject
```

### 4. Create an App

```bash
python manage.py startapp myapp
```

### 5. Add the App to Installed Apps

Edit the `settings.py` file inside `myproject` directory and add `myapp`:

```python
INSTALLED_APPS = [
    ...
    'myapp',
]
```

### 6. Apply Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Now, open your browser and go to `http://127.0.0.1:8000/`.

## Additional Resources

For more details, visit the [W3Schools Django tutorial](https://www.w3schools.com/django/).
😊