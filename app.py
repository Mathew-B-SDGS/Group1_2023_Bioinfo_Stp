from flask import Flask, request, render_template, session
from modules import test_api, PanelAppApi, ParserExcel, HGNC_converter

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
            api_calls_object = PanelAppApi.ApiCallsSadie(r_number)
            filtered_api_result = api_calls_object.return_specific_panel()

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


@app.route("/testapi", endpoint="testapi")
def test_data():
    # api_object_testapi =  ()
    return test_api.TestApi.allpanels()


@app.route("/allpanels", endpoint="allpanels")
def all_panels():
    # Create an instance of the ApiCallsSadie class
    api_calls_sadie = PanelAppApi.ApiCallsSadie()
    return api_calls_sadie.get_panels_for_genomic_test()

@app.route("/search/genelist",methods=['GET'], endpoint="genelist")
def gene_list():
    r_number = session.get('r')
    if r_number is not None:
        api_calls_object = PanelAppApi.ApiCallsSadie(r_number)
        filtered_api_result = api_calls_object.extract_genes_hgnc()
        list_of_genes = []
        return filtered_api_result
        # if filtered_api_result:
        #     for i in filtered_api_result:
        #         HGNC_converter_object = HGNC_converter.HgncConverter(i)
        #         json_object = HGNC_converter_object.ensembl_id_api_query(full_transcript_list=False)
        #         list_of_genes.append(HGNC_converter_object)
        #         del HGNC_converter_object, json_object
        #     return list_of_genes
        # return render_template("genelist.html", r=r_number, genes=list_of_genes)
    else:
        return "<p>No 'r' parameter found in the session</p>"

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
