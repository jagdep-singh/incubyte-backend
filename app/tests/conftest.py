import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.api.deps import get_db
from app.models.user import User
from app.core.security import hash_password


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


@pytest.fixture(scope="session", autouse=True)
def setup_users():
    db = next(get_db())

    admin = db.query(User).filter(User.email == "admin@sweetshop.com").first()
    if not admin:
        admin = User(
            email="admin@sweetshop.com",
            hashed_password=hash_password("admin123"),
            is_admin=True,
        )
        db.add(admin)

    user = db.query(User).filter(User.email == "user@test.com").first()
    if not user:
        user = User(
            email="user@test.com",
            hashed_password=hash_password("user123"),
            is_admin=False,
        )
        db.add(user)

    db.commit()


@pytest.fixture(scope="session")
def admin_token(client):
    res = client.post(
        "/api/auth/login",
        data={
            "username": "admin@sweetshop.com",
            "password": "admin123",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    return res.json()["access_token"]


@pytest.fixture(scope="session")
def user_token(client):
    res = client.post(
        "/api/auth/login",
        data={
            "username": "user@test.com",
            "password": "user123",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    return res.json()["access_token"]
