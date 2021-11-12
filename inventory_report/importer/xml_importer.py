from typing import List
from xml.etree import cElementTree as ET

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    """
    Class to import xml files
    """

    @classmethod
    def import_data(cls, file_path: str) -> List[dict]:
        """
        Method to import xml file and parse
        """
        cls._check_file_ext(file_path, "xml")

        # read file and get dataset tag
        dataset = list(ET.parse(file_path).getroot())

        # transform each record of list into a dict
        items = []

        for record in list(dataset):
            # map each child element into a key with value of dict
            items.append({el.tag: el.text for el in list(record)})

        return items
