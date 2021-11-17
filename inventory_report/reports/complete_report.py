from typing import List

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    """
    This class is used for generate the complete report
    """

    @classmethod
    def generate(cls, data: List[dict]) -> str:
        """
        This method receives a list of dict's and transform into the complex
        report as string
        """
        # complete report contains the simple report.
        complex_report = super().generate(data)

        # add a space and header of stock count list
        complex_report += "\nProdutos estocados por empresa: \n"

        # build stock count list
        for company_name, stock_count in cls.stock_count.items():
            complex_report += f"- {company_name}: {stock_count}\n"

        # return the report
        return complex_report
