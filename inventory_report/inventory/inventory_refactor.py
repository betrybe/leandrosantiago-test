from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor:
    """
    Refactor of Inventory class using DI
    """

    reports = {"simples": SimpleReport, "completo": CompleteReport}

    def __init__(self, importer: Importer):
        super().__init__()
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, file_path: str, report_type: str) -> str:
        """
        Read content of file and use importer passed on instanciate the class
        to generate the simple or complex report
        """
        # check which report will be generated
        report = self.reports[report_type]

        # import data from file path
        self.data += self.importer.import_data(file_path)

        # generate and return report
        return report.generate(self.data)
