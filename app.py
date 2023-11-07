from flask import Flask
from modules import test_api, PanelAppApi


app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<h1>This is the front end for out app so far</h1>
            <p>It's not much but it's a start</p>
            <a href="/test">Test data</a>
            <a href="/allpanels">All Panels</a>
            <a href="/test/1">Test Panel</a>
            """


@app.route("/test")
def test_data():
    return test_api.TestApi.allpanels()

@app.route("/test/<r>")
def test_panel(r):
    # Create an instance of the ApiCallsSadie class
    api_calls_sadie = PanelAppApi.ApiCallsSadie()
    return api_calls_sadie.return_specific_panel(r)

@app.route("/allpanels")
def all_panels():
    # Create an instance of the ApiCallsSadie class
    api_calls_sadie = PanelAppApi.ApiCallsSadie()
    return api_calls_sadie.get_panels_for_genomic_test()