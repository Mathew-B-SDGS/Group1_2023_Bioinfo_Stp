
# @app.route("/search/download150", endpoint="download150", methods=['POST'])
# def download_file():
#     selected_action = request.form['action']
#     r_code = session.get('r')
#     obj_for_bed = api_query_R.RCodeToBedFile(r_code, selected_action)
#     file_content = obj_for_bed.create_bed_file_iterable_150()
#     response = Response(file_content, content_type='text/plain');
#     file_name = f'generated_file_{r_code}.bed'
#     response.headers['Content-Disposition'] = f'attachment; filename={file_name}'
#     return response

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


# def pad_bed_files(self):
#     """Creates a bedfile structure for front end creation of bedfile"""
#     coords_for_bed = []
#     try:
#         for gene in self.get_coords_for_bed():
#             for entity in gene:
#                 chrom, start, end = entity
#                 if self.include_exon == 'True':
#                     start = int(start) - 50
#                     end = int(end) + 50
#                 line = str(chrom) + "\t" + str(start) + \
#                     "\t" + str(end) + "\n"
#                 coords_for_bed.append(line)
#         return coords_for_bed
#     except Exception as e:
#         return self.__str__() + f"\nError: {str(e)}"

# def create_bed_file_iterable_modified(self):
#     """Creates a bedfile structure for front end creation of bedfile"""
#     coords_for_bed = []
#     try:
#         for gene in self.get_coords_for_bed():
#             for entity in gene:
#                 chrom, start, end = entity
#                 if self.include_exon == 'True':
#                     # Ensure start is non-negative
#                     start = max(0, int(start) - 50)
#                     end = int(end) + 50
#                 coords_for_bed.append([str(chrom), int(start), int(end)])
#         return coords_for_bed
#     except Exception as e:
#         return self.__str__() + f"\nError: {str(e)}"
