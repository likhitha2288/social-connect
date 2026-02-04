Social Connect Backend API

A complete backend REST API for a social media–style application built using FastAPI, PostgreSQL, SQLAlchemy, and JWT Authentication.

This project supports user registration, login, authentication, posts, and voting functionality.

🚀 Features

User Registration & Login

Secure Password Hashing (bcrypt)

JWT Authentication

Create, Read Posts

Vote (Like/Unlike) Posts

Swagger UI for API testing

PostgreSQL Database

SQLAlchemy ORM

🛠 Tech Stack

Python 3.12

FastAPI

Uvicorn

PostgreSQL

SQLAlchemy

Passlib + bcrypt

JWT (OAuth2 Password Flow)

Project Structure
social-connect-backend/
app/
main.py
database.py
models.py
schemas.py
utils.py
oauth2.py
config.py
 routers/
  users.py
  auth.py
  posts.py
  vote.py
venv/
requirements.txt
README.md


