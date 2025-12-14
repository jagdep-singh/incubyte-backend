# Sweet Shop Management System (FastAPI)

## Overview
Backend API for managing a sweet shop using FastAPI, PostgreSQL, SQLAlchemy, and JWT authentication.

## Features
- User registration & login with JWT
- Role-based access (Admin / User)
- Sweet management (CRUD)
- Search sweets by name, category, price range
- Fully tested with pytest

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT (python-jose)
- Pytest

## Setup Instructions

### 1. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment variables
Create a `.env` file:
```
DATABASE_URL=postgresql://postgres:password@localhost:5432/sweetshop
JWT_SECRET=your_secret_key
```

### 4. Run migrations
```bash
alembic upgrade head
```

### 5. Start server
```bash
fastapi dev app/main.py
```

API Docs: http://127.0.0.1:8000/docs

## Testing
```bash
PYTHONPATH=. pytest -v
```

## API Endpoints

### Auth
- POST /api/auth/register
- POST /api/auth/login

### Sweets
- POST /api/sweets (Admin)
- GET /api/sweets
- GET /api/sweets/search
- PUT /api/sweets/{id} (Admin)
- DELETE /api/sweets/{id} (Admin)

## Notes
- Admin user is pre-seeded in tests
- JWT must be passed as Bearer token
