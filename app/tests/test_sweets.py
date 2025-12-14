def test_admin_create_sweet(client, admin_token):
    res = client.post(
        "/api/sweets/",
        json={
            "name": "Gulab Jamun",
            "category": "Indian",
            "price": 10.5,
            "quantity": 20,
        },
        headers={"Authorization": f"Bearer {admin_token}"},
    )
    assert res.status_code == 200
    assert res.json()["name"] == "Gulab Jamun"


def test_user_cannot_create_sweet(client, user_token):
    res = client.post(
        "/api/sweets/",
        json={
            "name": "Barfi",
            "category": "Indian",
            "price": 5.0,
            "quantity": 10,
        },
        headers={"Authorization": f"Bearer {user_token}"},
    )
    assert res.status_code == 403


def test_get_sweets(client):
    res = client.get("/api/sweets/")
    assert res.status_code == 200
    assert isinstance(res.json(), list)


def test_search_sweets(client):
    res = client.get("/api/sweets/search?name=Gulab")
    assert res.status_code == 200


def test_update_sweet_admin_only(client, admin_token):
    sweets = client.get("/api/sweets/").json()
    sweet_id = sweets[0]["id"]

    res = client.put(
        f"/api/sweets/{sweet_id}",
        json={"price": 15.0},
        headers={"Authorization": f"Bearer {admin_token}"},
    )
    assert res.status_code == 200
    assert res.json()["price"] == 15.0


def test_delete_sweet_admin_only(client, admin_token):
    sweets = client.get("/api/sweets/").json()
    sweet_id = sweets[0]["id"]

    res = client.delete(
        f"/api/sweets/{sweet_id}",
        headers={"Authorization": f"Bearer {admin_token}"},
    )
    assert res.status_code == 200
