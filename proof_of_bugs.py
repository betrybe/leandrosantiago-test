from inventory_report.inventory.inventory import Inventory

args = ["inventory_report/data/inventory.xml", "completo"]

expect = (
    "Data de fabricação mais antiga: 2019-09-06\n"
    "Data de validade mais próxima: 2022-09-17\n"
    "Empresa com maior quantidade de produtos estocados: "
    "Target Corporation\n\n"
    "Produtos estocados por empresa: \n"
    "- Target Corporation: 4\n"
    "- Galena Biopharma: 2\n"
    "- Cantrell Drug Company: 2\n"
    "- Moore Medical LLC: 1\n"
    "- REMEDYREPACK: 1\n"
)

result = Inventory.import_data(*args)
print(result)
