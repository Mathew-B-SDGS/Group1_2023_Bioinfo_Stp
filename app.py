from flask import Flask, request, render_template, session, Response
import os

from modules import ParserExcel, bedmake  # importing local modules ./modules/
# importing local blueprints ./AppBlueprints/
from AppBlueprints import database_blueprint, user_auth

# This is the main file that runs the app, it is the file that is run when you 
# run the command 'flask run'
# Below is the Factory function that creates the app, containing the app 
# routes and blueprints


def create_app(test_config=None):
    """
    IMPORTANT MAKE SURE TO INDENT ALL CODE IN THIS FUNCTION TO BE ALLIGNED

    This is a factory function that creates the app, changed to this as it
    is more flexible an allows us to change things in the config file without 
    having to change the code in this file. ]
    its also better if we want to deploy it anywhere else
    """

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='GoldSilverMoonStreamWoodpecker',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'), #ive commented this out as we are not using a database YET
    )

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
    all app routes are to be found below this comment
    including 
    - the home page
    - the search page
    - the gene list page
    - the download page
    
    """

    @app.route("/")
    def hello_world():
        """
        This is the home page route, it renders the home.html template with 
        links to search an R number and to go to the database or Auth pages 
        """
        return render_template("home.html")

    @app.route("/search", methods=['POST'])
    def test_data():
        """
        This is the search page route, it renders the search.html template with
        the search form and a link to the home page using the Data
        """
        if request.method == 'POST':
            r_code = request.form.get('r')
            session['r'] = r_code.upper()
            if r_code:
                # Create an object instance of the RCodeToBedFile class and
                # fetch the panel info
                bedmake_object = bedmake.RCodeToBedFile(
                    r_code, ref_genome='GRCh38')
                panel_information = bedmake_object.get_panel_for_genomic_test()
                panel_name = panel_information['name']
                panel_version = panel_information['version']

                # Create an object instance of the Parser class and parse the
                # NGTD excel file
                Parsed_results_object = ParserExcel.Parser()
                filtered_NGTD = Parsed_results_object.parse(r_code=r_code)

                # Create a dictionary to pass to the results.html template for
                # Jinja to render
                r_results_data = {"df": filtered_NGTD,
                                  "r_json": panel_information,
                                  "r": r_code.upper(),
                                  "panel_label": panel_name,
                                  "panel_version": panel_version}

                # if the api call has worked, render the results.html template
                # with results data
                if panel_information:
                    return render_template("results.html",
                                           results=r_results_data)
                else:
                    return "<p>Panel not found </p><a href='/'>Go back</a>"
            # Handle cases where 'r' is not provided or other issues
            return "<p>No data provided or invalid request</p>"
        # Inform users that a GET request is not supported
        return "<p>GET request is not supported. Use the search form.</P."

    @app.route("/search/genelist", methods=['GET'], endpoint="genelist")
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

    @app.route("/search/download", endpoint="download", methods=['POST'])
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

        api_calls_object = bedmake.RCodeToBedFile(
            r_code, ref_genome='GRCh38')
        panel_info = api_calls_object.get_panel_for_genomic_test()
        panel_name = panel_info['name']
        panel_name = panel_name.replace(' ', '_')
        panel_version = panel_info['version']

        # file_content_bytes = file_content_string.encode('utf-8')

        try:
            response = Response(
                output_content, content_type='text/plain; charset=utf-8')
            bases_pad = []
            entity = []
            if selected_padding == 'True':
                bases_pad = f'{bases}_bp_padding'
            else:
                bases_pad = 'no_padding'
            if exon_or_transcript == 'True':
                entity = 'MANE_exons'
            else:
                entity = 'MANE_transcript'

            name = f'{panel_name}_{panel_version}_{entity}_{bases_pad}.bed'
            attach = f'attachment; filename={name}'
            response.headers['Content-Disposition'] = attach
            return response
        except Exception as e:
            return f"Error: {str(e)}"

    """
    all blueprints are to be found below this comment
    (blueprints are modules of flask code that can be used to extend the app)
    including
    - the database blueprint
    - the Auth blueprint (not yet implemented)
    """
    # install the database blueprint into the module
    app.register_blueprint(database_blueprint.bp, url_prefix='/database')
    app.register_blueprint(user_auth.bp, url_prefix='/auth')
    return app
