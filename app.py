from flask import Flask, request, render_template, session, Response, Blueprint
import os
from appblueprints import database_blueprint
from modules import bedmake, parser_test_directory  # importing local modules ./modules/
# importing local blueprints 
from appblueprints import database_blueprint


"""
## This is the main app file ##

containing the create_app function and all the app routes.
this function is a factory function that creates the app.
therefore, all other components are placed in blueprints and imported into 
this file

"""


def create_app(test_config=None):
    """
    This is a factory function that creates the app, changed to this as it
    is more flexible an allows us to change things in the config file 
    without having to change the code in this file. 
    its also better if we want to deploy it anywhere else
    """

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config.
        SECRET_KEY='GoldSilverMoonStreamWoodpecker',
    )
    # set the database path to the project.db file
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'

    # ensure the instance folder exists
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    """
    all blueprints are to be found below this comment
    (blueprints are modules of flask code that can be used to extend the app)
    including
    - the database blueprint (database page)
    - the Base blueprint (home page)
    """

    # links the Base blueprint to the app
    app.register_blueprint(base, url_prefix='/')
    # links the database blueprint to the app
    app.register_blueprint(
        database_blueprint.blueprint_db, url_prefix='/database')

    # initialise the database and connect it to the app
    # from the /AppBlueprints/database_blueprint.py file
    database_blueprint.db.init_app(app)
    database_blueprint.create_tables(app.app_context(), database_blueprint.db)

    # finish the factory function by returning the app
    return app


"""
all app routes are to be found below this comment
including 
- the home page
- the search page
- the gene list page
- the download page

"""
# create the Base blueprint
base = Blueprint('base', __name__, url_prefix='/')


@base.route("/")
def hello_world():
    """
    This is the home page route, it renders the home.html template with 
    links to search an R number and to go to the database or Auth pages 
    """
    return render_template("home.html")


@base.route("/search", methods=['POST'])
def test_data():
    """
    This is the search page route, it renders the search.html template with
    the search form and a link to the home page using the Data
    """
    session.clear()
    if request.method == 'POST':
        r_code = request.form.get('r')
        session['r'] = r_code.upper()
        if r_code:
            # Create an object instance of the RCodeToBedFile class
            # and fetch the panel info
            bedmake_object = bedmake.RCodeToBedFile(
                r_code, ref_genome='GRCh38')
            panel_information = bedmake_object.get_panel_for_genomic_test()
            panel_name = panel_information['name']
            panel_version = panel_information['version']

            # Create an object instance of the Parser class
            # and parse the NGTD excel file
            parsed_results_object = parser_test_directory.Parser()
            filtered_NGTD = parsed_results_object.parse(r_code=r_code)

            # Create a dictionary to pass to the results.html template
            # for Jinja to render
            r_results_data = {"df": filtered_NGTD,
                              "r_json": panel_information,
                              "r": r_code.upper(),
                              "panel_label": panel_name,
                              "panel_version": panel_version}
            session['panel_name'] = panel_name
            session['panel_version'] = panel_version
            session['gene_list'] = [gene.get("gene_data", {}).get(
                "gene_symbol", "") for gene in panel_information.get("genes", [])]

            # = panel_information.get( "genes", [{}])[0].get("gene_data", {}).get("gene_symbol", "")

            # if the api call has worked, render the results.html template
            # with results data
            if panel_information:
                return render_template("results.html", results=r_results_data)
            else:
                return "<p>Panel not found </p><a href='/'>Go back</a>"
        # Handle cases where 'r' is not provided or other issues
        return "<p>No data provided or invalid request</p>"
    # Inform users that a GET request is not supported
    return "<p>GET request is not supported. Use the search form.</P."


@base.route("/search/genelist", methods=['GET'], endpoint="genelist")
def gene_list():
    r_code = session.get('r')
    if r_code is not None:
        bedmake_object = bedmake.RCodeToBedFile(
            r_code, ref_genome='GRCh38')
        panel_info = bedmake_object.get_panel_for_genomic_test()
        gene_name_panel = bedmake_object.extract_genes_hgnc()
        panel_name = panel_info['name']
        panel_version = panel_info['version']
        data_genepage = {"gene_list": gene_name_panel,
                         "panel_name": panel_name,
                         "panel_version": panel_version}
        return render_template("genelist.html", results=data_genepage)
    else:
        return "No 'r' parameter found in the session"


@base.route("/search/download", endpoint="download", methods=['POST'])
def download_file():
    r_code = session.get('r')
    # choose between GRCh38 or GRCh37
    selected_build = request.form['build']
    # choose between Mane Select transcript coordinates or exon coordinates
    exon_or_transcript = request.form['version']
    # add an additonal 50bp padding to the exons or transcript
    selected_padding = request.form['padding']
    # Number of bases to pad exon/transcript
    bases = request.form['base_num']

    obj_for_bed = bedmake.RCodeToBedFile(
        test_code=r_code,
        include_exon=exon_or_transcript,
        ref_genome=selected_build,
        padded=selected_padding,
        num_bases=bases)

    output_content = obj_for_bed.create_string_bed()

    bedmake_object = bedmake.RCodeToBedFile(
        r_code, ref_genome='GRCh38')
    panel_info = bedmake_object.get_panel_for_genomic_test()
    panel_name = panel_info['name']
    panel_name = panel_name.replace(' ', '_')
    panel_version = panel_info['version']

    # file_content_bytes = file_content_string.encode('utf-8')

    try:
        response = Response(
            output_content, content_type='text/plain; charset=utf-8')
        base_pad = []
        entity = []
        if exon_or_transcript == 'True':
            entity = 'MANE_exons'
        else:
            entity = 'MANE_transcript'
        if selected_padding == 'True':
            base_pad = f'{bases}_bp_padding'
        else:
            base_pad = 'no_padding'
        name = f'{panel_name}_{panel_version}_{entity}_{base_pad}.bed'
        attach = f'attachment; filename={name}'
        response.headers['Content-Disposition'] = attach
        return response
    except Exception as e:
        return f"Error: {str(e)}"
