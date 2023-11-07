import requests

class TestApi:
    def allpanels():
        """Returns all panels from PanelApp API"""
        base_url = "http://panelapp.genomicsengland.co.uk/api/v1"
        panel_url = base_url + "/panels/"
        response = requests.get(panel_url)
        if response.status_code == 200:
            return (response.json())
    
