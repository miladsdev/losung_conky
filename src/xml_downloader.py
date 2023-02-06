from datetime import date
import requests
import zipfile
import os
from pathlib import Path

class xml_downloader:
    def __init__(self, year) -> None:
        self.files = []
        self.year = year
        self.directory = str(Path.home()) + "/.config/losung_conky/"

    def run(self) -> None:

        if os.path.exists(self.directory + "data/Losung_%s_XML.zip" % date.today().year):
            return

        url = "https://www.losungen.de/fileadmin/media-losungen/download/Losung_%s_XML.zip" % self.year
        response = requests.get(url)

        if (os.path.exists(self.directory + "data/")):
            os.makedirs(path)

        with open(self.directory + "data/Losung_%s_XML.zip" % self.year, 'wb') as file:
            file.write(response.content)

        with zipfile.ZipFile(self.directory + "data/Losung_%s_XML.zip" % self.year, 'r') as zip_ref:
            zip_ref.extractall(self.directory + "data")
