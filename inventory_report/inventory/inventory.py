from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    """
    Class used to read file and print simple or complex report
    """

    importers = {"csv": CsvImporter, "json": JsonImporter, "xml": XmlImporter}
    reports = {"simples": SimpleReport, "completo": CompleteReport}

    @classmethod
    def import_data(cls, file_path: str, report_type: str) -> str:
        """
        Read content of file and use specific importer based on file extension
        to generate the simple or complex report
        """
        # get file extension
        _, file_ext = file_path.lower().split(".", -1)

        # check which importer will be used
        importer = cls.importers[file_ext]

        # check which report will be generated
        report = cls.reports[report_type]

        # import data from file path
        data = importer.import_data(file_path)

        # generate and return report
        return report.generate(data)
