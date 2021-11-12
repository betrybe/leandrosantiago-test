import json
from typing import List

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    """
    Class to import json file and parse
    """

    def import_data(self, file_path: str) -> List[dict]:
        """
        Method to import json file and parse
        """
        try:
            # read file in path
            with open(file_path) as json_file:
                # read and return content formated
                content = json.loads(json_file)
                return content
        except Exception:
            # when can't read file and return content throw specific error msg
            raise TypeError(f"Cannot import JSON file in path {file_path}")
