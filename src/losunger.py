import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path
from xml_downloader import xml_downloader
import os


class losunger:
    """
    gets the losung for today
    """

    def __init__(self) -> None:
        self.data_path = r'' + str(Path.home()) + "/.config/losung_conky/" + 'data/'
        self.files = self.list_xml_files()
        self.directory = str(Path.home()) + "/.config/losung_conky/"

    def list_xml_files(self):
        """
        returns a dictionary of .xml files in data directory:
            keys: year
            values: name of the file
        """

        # dict to store files
        files = {}

        # Iterate directory
        for path in os.listdir(self.data_path):
            # check if current path is a file
            p = os.path.join(self.data_path, path)
            if os.path.isfile(p) and p[-3:] == 'xml':
                files[int(path[-8:-4])] = path

        return files

    def get_losung(self, date_passed):
        """
        returns the losung for the date specified
        """

        if (date_passed.year not in self.files.keys()):
            return None

        tree = ET.parse(self.data_path + self.files[date_passed.year])
        root = tree.getroot()

        losung_today = {}
        for losung in root:
            for child in losung:
                if child.tag == 'Datum' and \
                        child.text[0:10] == date_passed.strftime("%Y-%m-%d"):
                    for i in losung:
                        losung_today[i.tag] = i.text

        return losung_today

xd = xml_downloader(date.today().year)
xd.run()

px = losunger()

losungstext = px.get_losung(date.today()).get("Losungstext") + "\n"
losungsvers = "- " + px.get_losung(date.today()).get("Losungsvers") + "\n\n"
lehrtext = px.get_losung(date.today()).get("Lehrtext") + "\n"
lehrtextvers = "- " + px.get_losung(date.today()).get("Lehrtextvers")

losung = losungstext + losungsvers + lehrtext + lehrtextvers

print(losung)
