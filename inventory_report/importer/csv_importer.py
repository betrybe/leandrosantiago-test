import csv
from typing import List

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    """
    Class to import csv file and parse
    """

    def import_data(self, file_path: str) -> List[dict]:
        """
        Method to import csv file and parse
        """
        try:
            # read file in path
            with open(file_path) as csv_file:
                # read and return content formated
                content = csv.DictReader(csv_file)
                return list(content)
        except Exception:
            # when can't read file and return content throw specific error msg
            raise TypeError(f"Cannot import CSV file in path {file_path}")
