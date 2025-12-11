from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_get_activities():
    res = client.get("/activities")
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_and_duplicate():
    email = "teststudent@mergington.edu"

    # Ensure signup succeeds
    res = client.post(f"/activities/Chess Club/signup", params={"email": email})
    assert res.status_code == 200
    assert "Signed up" in res.json().get("message", "")

    # Duplicate signup returns 400
    res_dup = client.post(f"/activities/Chess Club/signup", params={"email": email})
    assert res_dup.status_code == 400


def test_activity_not_found():
    res = client.post("/activities/Nonexistent/signup", params={"email": "x@y.z"})
    assert res.status_code == 404
