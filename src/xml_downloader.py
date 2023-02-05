from datetime import date
import requests
import zipfile
import os

class xml_downloader:
    def __init__(self, year) -> None:
        self.files = []
        self.year = year
    
    def run(self) -> None:

        if os.path.exists("data/Losung_%s_XML.zip" % date.today().year):
            return
        
        url = "https://www.losungen.de/fileadmin/media-losungen/download/Losung_%s_XML.zip" % self.year
        response = requests.get(url)

        with open("data/Losung_%s_XML.zip" % self.year, 'wb') as file:
            file.write(response.content)

        with zipfile.ZipFile("data/Losung_%s_XML.zip" % self.year, 'r') as zip_ref:
            zip_ref.extractall('data')

