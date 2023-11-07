import requests

# Specifying the API endpoint URL
api_url = "https://panelapp.genomicsengland.co.uk/api/v1/panels"

# Make a request to the API to retrieve the panels, with an filtering criteria
def get_panels_for_genomic_test(genomic_test_id):
    endpoint = f"{api_url}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve panels")
        return None
    
genomic_test_id = "R216"  # Replace with your test ID
panels = get_panels_for_genomic_test(genomic_test_id)

print(panels)


# Define a function to get a specific panel by its ID
def get_specific_panel(panels, panel_id):
    if panel_id in panels:
        return panels[panel_id]
    return None


# Specify the ID of the panel you want to retrieve
specific_panel_id = "R216"  # Replace with the actual panel ID

# Retrieve the specific panel
specific_panel = get_specific_panel(panels, specific_panel_id)

# Check if the panel was found and if it is then print its details
if specific_panel:
    print("Specific Panel:")
    print(json.dumps(specific_panel, indent=2))
else:
    print(f"Panel with ID {specific_panel_id} not found.")

# Define function for specific relevant disease and # Retrieve the relevant disorders, to get the R number
def get_relevant_disorders(panels,specific_panel_id, relevant_disorders)
    if relevant_disorders in panels:
        return relevant_disorders
    return None


