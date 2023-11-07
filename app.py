from flask import Flask, request, render_template
from modules import test_api, PanelAppApi


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/search", methods=['POST'])
def test_data():
    if request.method == 'POST':
        r = request.form.get('r')
        if r:
            # Create an instance of the ApiCallsSadie class and fetch the panel
            api_calls_sadie = PanelAppApi.ApiCallsSadie()
            result = api_calls_sadie.return_specific_panel(r)
            #check if the result has actually worked, Cant check for status code as its not a request module anymore
            if result:
                return result
            else:
                return "<p>Panel not found </p><a href='/'>Go back</a>"
        return "<p>No data provided or invalid request</p>"  # Handle cases where 'r' is not provided or other issues
    return "<p>GET request is not supported. Use the search form.</P."  # Inform users that a GET request is not supported

if __name__ == "__main__":
    app.run(debug=True)





# @app.route("/test")
# def test_data():
#     return test_api.TestApi.allpanels()

# @app.route("/test/<r>")
# def test_panel(r):
#     # Create an instance of the ApiCallsSadie class
#     api_calls_sadie = PanelAppApi.ApiCallsSadie()
#     return api_calls_sadie.return_specific_panel(r)

# @app.route("/allpanels")
# def all_panels():
#     # Create an instance of the ApiCallsSadie class
#     api_calls_sadie = PanelAppApi.ApiCallsSadie()
#     return api_calls_sadie.get_panels_for_genomic_test()


# @app.route("/test", methods=['GET', 'POST'])
# def test_data():
#     if request.method == 'POST':
#         r = request.form.get('r')
#         if r:
#             # Create an instance of the ApiCallsSadie class and fetch the panel
#             api_calls_sadie = PanelAppApi.ApiCallsSadie()
#         return api_calls_sadie.return_specific_panel(r)
