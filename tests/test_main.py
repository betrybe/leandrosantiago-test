import sys
from unittest.mock import patch

import pytest

from inventory_report.main import main

simple_out = (
    "Data de fabricação mais antiga: 2019-09-06\n"
    "Data de validade mais próxima: 2022-09-17\n"
    "Empresa com maior quantidade de produtos estocados: "
    "Target Corporation\n"
)

complete_out = (
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


def test_validar_menu_enviar_um_arquivo_csv_simples(capsys):
    args = ["0", "inventory_report/data/inventory.csv", "simples"]
    with patch.object(sys, "argv", args):
        main()
    out, _ = capsys.readouterr()
    assert simple_out == out


def test_validar_menu_enviar_um_arquivo_csv_completo(capsys):
    args = ["0", "inventory_report/data/inventory.csv", "completo"]
    with patch.object(sys, "argv", args):
        main()
    out, _ = capsys.readouterr()
    assert complete_out == out


def test_validar_menu_enviar_um_arquivo_json_simples(capsys):
    args = ["0", "inventory_report/data/inventory.json", "simples"]
    with patch.object(sys, "argv", args):
        main()
    out, _ = capsys.readouterr()
    assert simple_out == out


def test_validar_menu_enviar_um_arquivo_json_completo(capsys):
    args = ["0", "inventory_report/data/inventory.json", "completo"]
    with patch.object(sys, "argv", args):
        main()
    out, _ = capsys.readouterr()
    assert complete_out == out


def test_validar_menu_enviar_um_arquivo_xml_simples(capsys):
    args = ["0", "inventory_report/data/inventory.xml", "simples"]
    with patch.object(sys, "argv", args):
        main()
    out, _ = capsys.readouterr()
    assert simple_out == out


def test_validar_menu_enviar_um_arquivo_xml_completo(capsys):
    args = ["0", "inventory_report/data/inventory.xml", "completo"]
    with patch.object(sys, "argv", args):
        main()
    out, _ = capsys.readouterr()
    assert complete_out == out


def test_validar_menu_com_menos_argumentos(capsys):
    with pytest.raises(Exception) as err:
        args = ["inventory_report/data/inventory.json", ""]
        with patch.object(sys, "argv", args):
            main()
        _, err = capsys.readouterr()
        assert err == "Verifique os argumentos\n"
