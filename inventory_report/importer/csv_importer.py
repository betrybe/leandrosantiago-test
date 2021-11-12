import csv
from typing import List

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    """
    Class to import csv file and parse
    """

    @classmethod
    def import_data(cls, file_path: str) -> List[dict]:
        """
        Method to import csv file and parse
        """
        cls._check_file_ext(file_path, "csv")

        # read file in path
        with open(file_path) as csv_file:
            # read and return content formated
            content = csv.DictReader(csv_file)
            return list(content)
