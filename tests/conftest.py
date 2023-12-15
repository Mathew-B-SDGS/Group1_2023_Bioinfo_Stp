import pytest
from app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    # other setup can go here
    # set up database

    yield app

    # clean up / reset resources here

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_home_page(client):
    response = client.get("/")
    assert b"<h1>Welcome to PanelSearcher!</h1>" in response.data


def test_panel_search(client):
    response = client.post("/search", data={
        "r": "R167"
    })
    assert response.status_code == 200
    assert b"<h2>Panel name: Autosomal recessive primary hypertrophic osteoarthropathy</h2>" in response.data


def test_bed_download(client):
    response = client.post("/search/download", data={
        "build": "GRCh38",
        "version": "True",
        "padding": "True",
        "base_num": "75"
    })
    assert response.status_code == 200
