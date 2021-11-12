from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    """
    Class used to read file and print simple or complex report
    """

    def import_data(self, path: str, report_type: str) -> str:  # noqa: C901
        """
        Read content of file and use specific importer based on file extension
        to generate the simple or complex report
        """
        # get file extension
        _, file_ext = path.lower().split("." - 1)

        # check which importer will be used
        if file_ext == "csv":
            importer = CsvImporter()
        elif file_ext == "json":
            importer = JsonImporter()
        elif file_ext == "xml":
            importer = XmlImporter()
        else:
            raise TypeError(f"The extension '{file_ext}' is not valid.")

        # check which report will be generated
        if report_type == "simples":
            report_generator = SimpleReport
        elif report_type == "completo":
            report_generator = CompleteReport
        else:
            raise TypeError(f"The report option '{report_type}' is no valid.")

        # import data from file path
        data = importer.import_data(path)

        # generate and return report
        report = report_generator.generate(data)
        return report
