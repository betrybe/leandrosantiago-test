from datetime import datetime
from typing import List

DATE_FORMAT = "%Y-%m-%d"


class SimpleReport:
    """
    This class is used for generate the simple report
    """

    oldest_man_date: datetime
    closest_exp_date: datetime
    max_stock_name: str
    stock_count: dict = {}

    def __parse_item(item: dict) -> List[datetime, datetime, str]:
        """
        Simplify parsing and extraction fields method.
        """
        man_date = datetime.strptime(item["data_de_fabricacao"], DATE_FORMAT)
        exp_date = datetime.strptime(item["data_de_validade"], DATE_FORMAT)
        com_name = item["nome_da_empresa"]

        return man_date, exp_date, com_name

    @classmethod
    def generate(cls, list: List[dict]) -> str:  # noqa: C901
        """
        This method receives a list of dict's and transform into the simple
        report as string
        """
        # need some item to print report
        if not list or len(list) < 1:
            raise ValueError("Can't generate report without data.")

        # to print index of item if throw
        i = 0

        try:
            # to optimize, the first item no need check
            (
                cls.oldest_man_date,
                cls.closest_exp_date,
                cls.max_stock_name,
            ) = cls.__parse_item(list[i])

            # restart stock_count and count 1 item for first company
            cls.stock_count = {f"{cls.max_stock_name}": 1}

            # compare all items to find values of report
            for i, item in enumerate(list[1:]):
                man_date, exp_date, com_name = cls.__parse_item(item)

                # check oldest manufactury date
                if man_date < cls.oldest_man_date:
                    cls.oldest_man_date = man_date

                # check closest expiration date
                if exp_date > cls.closest_exp_date:
                    SimpleReport.closest_exp_date = exp_date

                # count items of company
                cls.stock_count[com_name] = (
                    cls.stock_count.get(com_name, 0) + 1
                )

            # get company name with biggest stock
            cls.max_stock_name = max(cls.stock_count, key=cls.stock_count.get)

            # format dates
            oldest_man_formated = cls.oldest_man_date.strftime(DATE_FORMAT)
            closest_exp_formated = cls.closest_exp_date.strftime(DATE_FORMAT)

            # build and return the report
            simple_report = (
                f"Data de fabricação mais antiga: {oldest_man_formated}\n"
                f"Data de validade mais próxima: {closest_exp_formated}\n"
                "Empresa com maior quantidade de produtos estocados: "
                f"{cls.max_stock_name}\n"
            )

            return simple_report
        except ValueError:
            raise TypeError(f"Invalid item[{i}] format.")
        except Exception as e:
            raise Exception(f"An unknown error occurred. {e}")
