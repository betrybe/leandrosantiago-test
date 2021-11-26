import sys

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    # check if have 2 arguments
    if len(sys.argv) != 3:
        # expected message in test...
        raise Exception("Verifique os argumentos\n")

    _, file_path, report_type = sys.argv

    # map importers with extensions
    importers = {"csv": CsvImporter, "json": JsonImporter, "xml": XmlImporter}

    # get file extension
    _, file_ext = file_path.lower().split(".", -1)

    # create instance of inventory refactor
    inventory = InventoryRefactor(importers[file_ext])

    # generate report
    result = inventory.import_data(file_path, report_type)

    # and print
    print(result, end="")
