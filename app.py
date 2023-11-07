from flask import Flask
from modules import test_api
app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<h1>This is the front end for out app so far</h1>
            <p>It's not much but it's a start</p>
            <a href="/test">Test data</a>
            """


@app.route("/test")
def test_data():
    return test_api.TestApi.allpanels()

@app.route("/test/<int:panel_id>")
def test_panel(panel_id):
    return test_api.TestApi.panel(panel_id)