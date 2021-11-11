from typing import Dict, List

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    """
    This class is used for generate the complete report
    """

    @classmethod
    def generate(cls, list: List[Dict]) -> str:
        """
        This method receives a list of dict's and transform into the complex
        report as string
        """
        # complete report contains the simple report.
        complex_report = super().generate(list)

        # add a space and header of stock count list
        complex_report += "\n\nProdutos estocados por empresa:\n"

        # build stock count list
        for company_name, stock_count in cls.stock_count.items():
            complex_report += f"- {company_name}: {stock_count}"

        # return the report
        return complex_report
