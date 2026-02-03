def test_get_activities(client):
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    # Basic sanity checks
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_and_double_signup(client):
    activity = "Basketball Team"
    email = "alice@mergington.edu"

    # First signup should succeed
    r = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert r.status_code == 200
    assert "Signed up" in r.json().get("message", "")

    # Second signup should fail with 400
    r2 = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert r2.status_code == 400


def test_unregister_flow(client):
    activity = "Basketball Team"
    email = "bob@mergington.edu"

    # Signup first
    r = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert r.status_code == 200

    # Unregister should succeed
    r2 = client.post(f"/activities/{activity}/unregister", params={"email": email})
    assert r2.status_code == 200
    assert "Unregistered" in r2.json().get("message", "")

    # Unregister again should return 404
    r3 = client.post(f"/activities/{activity}/unregister", params={"email": email})
    assert r3.status_code == 404


def test_unregister_nonexistent_activity(client):
    r = client.post("/activities/Nonexistent/unregister", params={"email": "x@y"})
    assert r.status_code == 404
