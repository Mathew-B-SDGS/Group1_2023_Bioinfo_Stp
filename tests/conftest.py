import pytest
from app import create_app

"""
conftest.py is the standard file name for a flasking testing app
"""


@pytest.fixture()
def app():
    """Set up app for testing, import app from app.py"""
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    """Return app for testing"""
    return app.test_client()


def test_home_page(client):
    """Test that the home page title appears when you load the app"""
    response = client.get("/")
    assert b"<h1>Welcome to PanelSearcher v1.0!</h1>" in response.data


def test_panel_search(client):
    """Check you get the correct panel related to the R test code"""
    response = client.post("/search", data={
        "r": "R167"
    })
    assert response.status_code == 200
    assert (b"<h2>Panel name: Autosomal recessive primary hypertrophic"
            b" osteoarthropathy</h2>" in response.data)
