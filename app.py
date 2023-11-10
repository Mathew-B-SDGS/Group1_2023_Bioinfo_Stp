from flask import Flask, request, render_template, session , Response
from modules import ParserExcel, HGNC_converter , api_query_R

app = Flask(__name__)
app.debug = True
app.secret_key = "GoldSilverMoonStreamWoodpecker"

@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/search", methods=['POST'])
def test_data():
    if request.method == 'POST':
        r_number = request.form.get('r')
        session['r'] = r_number
        if r_number:
            # Create an object instance of the ApiCallsSadie class and fetch the panel
            api_calls_object = api_query_R.ApiCallsbyR(r_number)
            filtered_api_result = api_calls_object.get_panel_for_genomic_test()

            # Create an object instance of the Parser class and parse the excel file
            Parsed_results_object = ParserExcel.Parser()
            filtered_df = Parsed_results_object.parse(r_number=r_number)

            # Create a dictionary to pass to the results.html template for Jinja to render
            jina_data = {"df": filtered_df,
                         "r_json": filtered_api_result, "r": r_number}

            # if the api call has worked, render the results.html template with Jinja data
            if filtered_api_result:
                return render_template("results.html", results=jina_data)
            else:
                return "<p>Panel not found </p><a href='/'>Go back</a>"
        # Handle cases where 'r' is not provided or other issues
        return "<p>No data provided or invalid request</p>"
    # Inform users that a GET request is not supported
    return "<p>GET request is not supported. Use the search form.</P."


@app.route("/search/genelist",methods=['GET'], endpoint="genelist")
def gene_list():
    r_number = session.get('r')
    if r_number is not None:
        api_calls_object = api_query_R.ApiCallsbyR(r_number)
        filtered_api_result = api_calls_object.extract_genes_hgnc()
        return filtered_api_result
    else:
        return "<p>No 'r' parameter found in the session</p>"

@app.route("/search/download", endpoint="download")
def download_file():
    r_number = session.get('r')
    obj_for_bed = api_query_R.ApiCallsbyR(r_number, 'GRCh37')
    file_content = obj_for_bed.create_bed_file_iterable()
    response = Response(file_content, content_type='text/plain');
    file_name = f'generated_file_{r_number}.bed'
    response.headers['Content-Disposition'] = f'attachment; filename={file_name}'
    return response

@app.route("/search/download", endpoint="download150")
def download_file():
    r_number = session.get('r')
    obj_for_bed = api_query_R.ApiCallsbyR(r_number, 'GRCh37')
    file_content = obj_for_bed.create_bed_file_iterable()
    response = Response(file_content, content_type='text/plain');
    file_name = f'generated_file_{r_number}.bed'
    response.headers['Content-Disposition'] = f'attachment; filename={file_name}'
    return response

if __name__ == "__main__":
    app.run(debug=True)


# @app.route("/test", methods=['GET', 'POST'])
# def test_data():
#     if request.method == 'POST':
#         r = request.form.get('r')
#         if r:
#             # Create an instance of the ApiCallsSadie class and fetch the panel
#             api_calls_sadie = PanelAppApi.ApiCallsSadie()
#         return api_calls_sadie.return_specific_panel(r)

# @app.route("/search", methods=['POST'])
# def test_data():
#     if request.method == 'POST':
#         r = request.form.get('r')
#         if r:
#             # Create an instance of the ApiCallsSadie class and fetch the panel
#             api_calls_sadie = PanelAppApi.ApiCallsSadie()
#             result = api_calls_sadie.return_specific_panel(r)
#             #check if the result has actually worked, Cant check for status code as its not a request module anymore
#             if result:
#                 return result
#             else:
#                 return "<p>Panel not found </p><a href='/'>Go back</a>"
#         return "<p>No data provided or invalid request</p>"  # Handle cases where 'r' is not provided or other issues
#     return "<p>GET request is not supported. Use the search form.</P."  # Inform users that a GET request is not supported

# @app.route("/testapi", endpoint="testapi")
# def test_data():
#     # api_object_testapi =  ()
#     return test_api.TestApi.allpanels()


# @app.route("/allpanels", endpoint="allpanels")
# def all_panels():
#     # Create an instance of the ApiCallsSadie class
#     api_calls_sadie = PanelAppApi.ApiCallsSadie()
#     return api_calls_sadie.get_panels_for_genomic_test()
