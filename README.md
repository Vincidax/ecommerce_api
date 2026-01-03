# E-commerce Product API

## Overview

This is a **Django REST Framework API** for managing an e-commerce platform’s products, categories, and users.  
It allows users to **view products and categories**, and **admins** to **create, update, and delete** products and categories.

The API also includes a **search feature** to find products by name or category, and a **home endpoint** that directs users to the main resources.

This project is built as a **class project** and deployed on **PythonAnywhere**.

---

## Features

- **CRUD operations** for:
  - Products
  - Categories
  - Users
- **Search products** by name or category
- **Home endpoint** to navigate the API
- Uses **Django ORM** for database interactions
- **Browsable API** via Django REST Framework

---

## Technologies Used

- Python 3.10+
- Django 6.0+
- Django REST Framework
- SQLite (local development)
- PythonAnywhere (deployment)

---

## Installation (Local Development)

1. **Clone the repository**

```bash
git clone https://github.com/vincidax/ecommerce_api.git
cd ecommerce-api
```

2. **Create a virtual environment using pipenv**

```bash
pip install pipenv
pipenv shell
```

3. **Install dependencies**

```bash
pipenv install
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Create a superuser (admin)**

```bash
python manage.py createsuperuser
```

Visit http://127.0.0.1:8000/ for the home endpoint.

---

## API Endpoints

### Home Endpoint

- **GET /**
  Returns links to main resources: Products, Categories, and Users

```json
{
  "products": "http://127.0.0.1:8000/api/products/",
  "categories": "http://127.0.0.1:8000/api/categories/",
  "users": "http://127.0.0.1:8000/api/users/",
  "message": "Welcome to the E-commerce API! Use these endpoints to explore."
}
```

### Products

- **GET /api/products/** → List all products
- **POST /api/products/** → Create a new product
- **GET /api/products/{id}/** → Retrieve product details
- **PUT/PATCH /api/products/{id}/** → Update product
- **DELETE /api/products/{id}/** → Delete product
- **Search:** /api/products/?search=product_name_or_category

### Categories

- **GET /api/categories/** → List all categories
- **POST /api/categories/** → Create a new category
- **GET /api/categories/{id}/** → Retrieve category details
- **PUT/PATCH /api/categories/{id}/** → Update category
- **DELETE /api/categories/{id}/** → Delete category

### Users

- **GET /api/users/** → List all users
- **POST /api/users/** → Create a new user
- **GET /api/users/{id}/** → Retrieve user details
- **PUT/PATCH /api/users/{id}/** → Update user
- **DELETE /api/users/{id}/** → Delete user

---

## Testing the API

You can use Postman or DRF browsable API:

1. Visit `http://127.0.0.1:8000/` for home links
2. Use `/api/products/` to list products
3. Use `/api/products/?search=iphone` to search products

---

## Deployment

The project is deployed on **PythonAnywhere**:

```
https://vincidax.pythonanywhere.com/
```

- Home endpoint: /

- API endpoints: `/api/products/`, `/api/categories/`, `/api/users/`

- Admin interface: `/admin/` (login with superuser credentials)

---

## Project Structure

ecommerce-api/
├── ecommerce/ # Django project settings
├── products/ # Products app
│ ├── models.py
│ ├── serializers.py
│ └── views.py
├── users/ # Users app
├── templates/ # HTML templates (optional)
├── staticfiles/ # Static files (CSS, JS)
├── manage.py
├── Pipfile
├── Pipfile.lock
├── db.sqlite3
└── README.md

---

Author: Vincent DUSHIME
GitHub: https://github.com/vincidax
