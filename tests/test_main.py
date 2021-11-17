import sys
from unittest.mock import patch

import pytest

from inventory_report.main import main


def test_validar_menu_enviar_um_arquivo_csv_simples(capsys):
    args = ["0", "inventory_report/data/inventory.csv", "simples"]
    with patch.object(sys, "argv", args):
        main()
    out, err = capsys.readouterr()

    assert "Data de fabricação mais antiga: 2019-09-06\n" in out
    assert "Data de validade mais próxima: 2022-09-17\n" in out
    assert "Empresa com maior quantidade de produtos estocados: " in out
    assert "Target Corporation\n" in out


def test_validar_menu_enviar_um_arquivo_csv_completo(capsys):
    args = ["0", "inventory_report/data/inventory.csv", "completo"]
    with patch.object(sys, "argv", args):
        main()
    out, err = capsys.readouterr()

    assert "Data de fabricação mais antiga: 2019-09-06\n" in out
    assert "Data de validade mais próxima: 2022-09-17\n" in out
    assert "Empresa com maior quantidade de produtos estocados: " in out
    assert "Target Corporation\n\n" in out
    assert "Produtos estocados por empresa: \n" in out
    assert "- Target Corporation: 4\n" in out
    assert "- Galena Biopharma: 2\n" in out
    assert "- Cantrell Drug Company: 2\n" in out
    assert "- Moore Medical LLC: 1\n" in out
    assert "- REMEDYREPACK: 1\n" in out


def test_validar_menu_enviar_um_arquivo_json_simples(capsys):
    args = ["0", "inventory_report/data/inventory.json", "simples"]
    with patch.object(sys, "argv", args):
        main()
    out, err = capsys.readouterr()

    assert "Data de fabricação mais antiga: 2019-09-06\n" in out
    assert "Data de validade mais próxima: 2022-09-17\n" in out
    assert "Empresa com maior quantidade de produtos estocados: " in out
    assert "Target Corporation\n" in out


def test_validar_menu_enviar_um_arquivo_json_completo(capsys):
    args = ["0", "inventory_report/data/inventory.json", "completo"]
    with patch.object(sys, "argv", args):
        main()
    out, err = capsys.readouterr()

    assert "Data de fabricação mais antiga: 2019-09-06\n" in out
    assert "Data de validade mais próxima: 2022-09-17\n" in out
    assert "Empresa com maior quantidade de produtos estocados: " in out
    assert "Target Corporation\n\n" in out
    assert "Produtos estocados por empresa: \n" in out
    assert "- Target Corporation: 4\n" in out
    assert "- Galena Biopharma: 2\n" in out
    assert "- Cantrell Drug Company: 2\n" in out
    assert "- Moore Medical LLC: 1\n" in out
    assert "- REMEDYREPACK: 1\n" in out


def test_validar_menu_enviar_um_arquivo_xml_simples(capsys):
    args = ["0", "inventory_report/data/inventory.xml", "simples"]
    with patch.object(sys, "argv", args):
        main()
    out, err = capsys.readouterr()

    assert "Data de fabricação mais antiga: 2019-09-06\n" in out
    assert "Data de validade mais próxima: 2022-09-17\n" in out
    assert "Empresa com maior quantidade de produtos estocados: " in out
    assert "Target Corporation\n" in out


def test_validar_menu_enviar_um_arquivo_xml_completo(capsys):
    args = ["0", "inventory_report/data/inventory.xml", "completo"]
    with patch.object(sys, "argv", args):
        main()
    out, err = capsys.readouterr()

    assert "Data de fabricação mais antiga: 2019-09-06\n" in out
    assert "Data de validade mais próxima: 2022-09-17\n" in out
    assert "Empresa com maior quantidade de produtos estocados: " in out
    assert "Target Corporation\n\n" in out
    assert "Produtos estocados por empresa: \n" in out
    assert "- Target Corporation: 4\n" in out
    assert "- Galena Biopharma: 2\n" in out
    assert "- Cantrell Drug Company: 2\n" in out
    assert "- Moore Medical LLC: 1\n" in out
    assert "- REMEDYREPACK: 1\n" in out


def test_validar_menu_com_menos_argumentos(capsys):
    with pytest.raises(Exception) as err:
        args = ["inventory_report/data/inventory.json", ""]
        with patch.object(sys, "argv", args):
            main()
        print(err)
        out, err = capsys.readouterr()
        assert "Verifique os argumentos" in err
