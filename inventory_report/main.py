import sys

from inventory_report.inventory.inventory import Inventory


def main():
    # check if have 2 arguments
    if len(sys.argv) != 3:
        # expected message in test...
        raise Exception("Verifique os argumentos\n")

    # passing args to class method
    print(Inventory.import_data(*sys.argv[1:]))
