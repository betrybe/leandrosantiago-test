import sys
from unittest.mock import patch

import pytest

from inventory_report.main import main


def test_validar_menu_enviar_um_arquivo_csv_simples(capsys):
    with patch.object(
        sys, "argv", ["0", "inventory_report/data/inventory.csv", "simples"]
    ):
        main()
    out, err = capsys.readouterr()

    assert "Data de fabricação mais antiga: 2019-09-06" in out
    assert "Data de validade mais próxima: 2022-09-17" in out
    assert "Data de validade mais próxima: 2022-09-17" in out
    assert (
        "Empresa com maior quantidade de produtos estocados: "
        "Target Corporation"
    ) in out


def test_validar_menu_enviar_um_arquivo_csv_completo(capsys):
    with patch.object(
        sys, "argv", ["0", "inventory_report/data/inventory.csv", "completo"]
    ):
        main()
    out, err = capsys.readouterr()
    assert "Data de fabricação mais antiga: 2019-09-06" in out
    assert "Data de validade mais próxima: 2022-09-17" in out
    assert (
        "Empresa com maior quantidade de produtos estocados: "
        "Target Corporation"
    ) in out
    assert "Produtos estocados por empresa: " in out
    assert "- Target Corporation: 4" in out
    assert "- Galena Biopharma: 2" in out
    assert "- Cantrell Drug Company: 2" in out
    assert "- Moore Medical LLC: 1" in out
    assert "- REMEDYREPACK: 1" in out


def test_validar_menu_enviar_um_arquivo_json_simples(capsys):
    with patch.object(
        sys, "argv", ["0", "inventory_report/data/inventory.json", "simples"]
    ):
        main()
    out, err = capsys.readouterr()

    assert "Data de fabricação mais antiga: 2019-09-06" in out
    assert "Data de validade mais próxima: 2022-09-17" in out
    assert (
        "Empresa com maior quantidade de produtos estocados: "
        "Target Corporation"
    ) in out


def test_validar_menu_enviar_um_arquivo_json_completo(capsys):
    with patch.object(
        sys, "argv", ["0", "inventory_report/data/inventory.json", "completo"]
    ):
        main()
    out, err = capsys.readouterr()

    assert "Data de fabricação mais antiga: 2019-09-06" in out
    assert "Data de validade mais próxima: 2022-09-17" in out
    assert (
        "Empresa com maior quantidade de produtos estocados: "
        "Target Corporation"
    ) in out
    assert "Produtos estocados por empresa: " in out
    assert "- Target Corporation: 4" in out
    assert "- Galena Biopharma: 2" in out
    assert "- Cantrell Drug Company: 2" in out
    assert "- Moore Medical LLC: 1" in out
    assert "- REMEDYREPACK: 1" in out


def test_validar_menu_enviar_um_arquivo_xml_simples(capsys):
    with patch.object(
        sys, "argv", ["0", "inventory_report/data/inventory.xml", "simples"]
    ):
        main()
    out, err = capsys.readouterr()

    assert "Data de fabricação mais antiga: 2019-09-06" in out
    assert "Data de validade mais próxima: 2022-09-17" in out
    assert (
        "Empresa com maior quantidade de produtos estocados: "
        "Target Corporation"
    ) in out


def test_validar_menu_enviar_um_arquivo_xml_completo(capsys):
    with patch.object(
        sys, "argv", ["0", "inventory_report/data/inventory.xml", "completo"]
    ):
        main()
    out, err = capsys.readouterr()
    assert "Data de fabricação mais antiga: 2019-09-06" in out
    assert "Data de validade mais próxima: 2022-09-17" in out
    assert (
        "Empresa com maior quantidade de produtos estocados: "
        "Target Corporation"
    )
    assert "Produtos estocados por empresa: " in out
    assert "- Target Corporation: 4" in out
    assert "- Galena Biopharma: 2" in out
    assert "- Cantrell Drug Company: 2" in out
    assert "- Moore Medical LLC: 1" in out
    assert "- REMEDYREPACK: 1" in out


def test_validar_menu_com_menos_argumentos(capsys):
    with pytest.raises(Exception):
        with patch.object(
            sys, "argv", ["inventory_report/data/inventory.json", ""]
        ):
            main()
        _, err = capsys.readouterr()
        assert err == "Verifique os argumentos"
