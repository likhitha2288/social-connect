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

📂 Project Structure
social-connect-backend/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── utils.py
│   ├── oauth2.py
│   ├── config.py
│   └── routers/
│       ├── users.py
│       ├── auth.py
│       ├── posts.py
│       └── vote.py
│
├── venv/
├── requirements.txt
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/social-connect-backend.git
cd social-connect-backend
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
If bcrypt errors occur, use:
pip install passlib==1.7.4 bcrypt==3.2.0
4️⃣ Configure Database
Update .env or config.py with your PostgreSQL credentials:
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=yourpassword
DATABASE_NAME=social_connect
DATABASE_USERNAME=postgres
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
5️⃣ Start the Server
uvicorn app.main:app --reload
Server will run at:
http://127.0.0.1:8000
📘 Swagger UI
Open your browser and go to:
http://127.0.0.1:8000/docs

Use Swagger UI to test all APIs.
