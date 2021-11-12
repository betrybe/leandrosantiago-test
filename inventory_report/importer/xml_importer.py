from typing import List
from xml.etree import cElementTree as ET

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    """
    Class to import xml files
    """

    def import_data(self, file_path: str) -> List[dict]:  # noqa: C901
        """
        Method to import xml file and parse
        """
        try:
            # read file and get dataset tag
            element_dataset = list(ET.parse(file_path).getroot())

            # transform each record of list into a dict
            content = []
            for element_record in list(element_dataset):
                # map each child element into a key with value of dict
                dict_record = {}
                for el_field in list(element_record):
                    # when field is numeric parse this
                    if el_field.text.isnumeric():
                        dict_record[el_field.tag] = int(el_field.text)
                    else:
                        dict_record[el_field.tag] = el_field.text

                content.append(dict_record)
            return content
        except Exception:
            # when can't read file and return content throw specific error msg
            raise TypeError(f"Cannot import XML file in path {file_path}")
