import json
from typing import List

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    """
    Class to import json file and parse
    """

    @classmethod
    def import_data(cls, file_path: str) -> List[dict]:
        """
        Method to import json file and parse
        """
        cls._check_file_ext(file_path, "json")

        # read file in path
        with open(file_path) as json_file:
            # read and return content formated
            content = json.load(json_file)
            return content
