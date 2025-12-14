def test_register_and_login(client):
    email = "unique_user_123@test.com"
    password = "password123"

    res = client.post(
        "/api/auth/register",
        json={"email": email, "password": password},
    )
    assert res.status_code == 200
    assert "access_token" in res.json()

    res = client.post(
        "/api/auth/login",
        data={
            "username": email,
            "password": password,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert res.status_code == 200
    assert "access_token" in res.json()
