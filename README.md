E-Commerce Backend – ProDev BE

A production-ready backend system built with Django, PostgreSQL, and JWT Authentication.
This project simulates a real-world backend engineering environment focused on performance, scalability, and API design.

🚀 Overview

This backend powers an e-commerce product catalog system with features such as:

Secure JWT-powered user authentication

CRUD operations for products and categories

Efficient filtering, sorting, and pagination

Well-structured API documentation (Swagger/OpenAPI)

Optimized relational database schema with indexing

It mimics real workplace expectations for backend developers—clean architecture, version control discipline, and production-grade API design.

🎯 Project Goals
✔ 1. CRUD APIs

Products

Categories

User accounts (Sign up, Login, Profile)

✔ 2. Advanced API Features

Filtering (e.g. category, price range)

Sorting (price, date)

Pagination (limit/offset or DRF pagination)

Keyword search

✔ 3. Database Optimization

Effective schema design

Query optimization

Indexing for high-performance lookups

🛠 Technologies Used
Technology	Purpose
Django	Backend framework
Django REST Framework (DRF)	API development
PostgreSQL	Relational database
JWT (SimpleJWT)	Authentication
Swagger / drf-yasg	API documentation
PythonAnywhere / Render	Deployment
⭐ Key Features
🔐 1. User Authentication (JWT)

Registration

Login

Token refresh

Protected endpoints

📦 2. Product & Category Management

Admins can create, update, delete

Public can view product catalog

🔎 3. Filtering & Sorting

Examples:

/products/?category=phones
/products/?min_price=100&max_price=500
/products/?sort=price_asc

📄 4. Pagination

Efficient response structure:

{
  "count": 120,
  "next": "/products/?page=2",
  "previous": null,
  "results": [...]
}

🧾 5. API Documentation

Automatically generated at:

/swagger/
/redoc/

🏗 Project Structure
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
├── products/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
├── requirements.txt
└── README.md

⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/PhilipTheBackendDeveloper/alx-project-nexus
cd alx-project-nexus

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables

Create .env:

SECRET_KEY=your_secret_key
DATABASE_NAME=ecommerce
DATABASE_USER=postgres
DATABASE_PASSWORD=yourpassword
DATABASE_HOST=localhost
DATABASE_PORT=5432

5. Run Migrations
python manage.py migrate

6. Start Server
python manage.py runserver

🧪 API Endpoints Overview
Authentication
Method	Endpoint	Description
POST	/auth/register/	Create user
POST	/auth/login/	Login & get JWT
POST	/auth/refresh/	Refresh token
Products
Method	Endpoint	Description
GET	/products/	List products
POST	/products/	Create product
GET	/products/<id>/	Retrieve product
PUT	/products/<id>/	Update product
DELETE	/products/<id>/	Delete product

Filters & sorting supported.

Categories
Method	Endpoint	Description
GET	/categories/	List categories
POST	/categories/	Create category
📘 Documentation

After running the server, visit:

🔹 Swagger UI:
/swagger/

🔹 ReDoc:
/redoc/

📤 Deployment

The API can be deployed on:

PythonAnywhere

Render

Railway

AWS EC2

Docker

Environment variables must be set appropriately for production.

📝 Git Commit Workflow (Used in This Project)
feat: set up Django project with PostgreSQL
feat: implement user authentication with JWT
feat: add product CRUD APIs
feat: add filtering, sorting, pagination
feat: integrate Swagger documentation
perf: optimize queries with indexing
docs: write full README and API instructions

🧠 Evaluation Criteria
✔ Functionality

All CRUD operations

Proper filtering & pagination

Secure authentication

✔ Code Quality

Clean structure + reusable components

Following Django best practices

Documented codebase

✔ User Experience

Easily navigable API documentation

✔ Version Control

Clear commit messages

Organized repo structure

👨‍💻 Author

Philip Odame Ayesu
Backend Developer