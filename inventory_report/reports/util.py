from datetime import datetime
from typing import Dict, List

DATE_FORMAT = "%Y-%m-%d"


def parse_item(item: Dict) -> List[datetime, datetime, str]:
    """
    Simplify parsing and extraction fields method.
    """
    man_date = datetime.strptime(item["data_de_fabricacao"], DATE_FORMAT)
    exp_date = datetime.strptime(item["data_de_validade"], DATE_FORMAT)
    com_name = item["nome_da_empresa"]

    return man_date, exp_date, com_name
