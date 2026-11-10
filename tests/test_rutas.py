from pathlib import Path

import pytest

from src.algoritmos import reconstruir_ruta, ruta_mas_rapida
from src.grafo import Grafo
from src.persistencia import cargar_grafo

RAIZ = Path(__file__).resolve().parents[1]


def test_ruta_del_ejemplo_del_informe():
    grafo = cargar_grafo(RAIZ / "datos" / "alto_magdalena.csv")
    ruta, minutos = ruta_mas_rapida(grafo, "0", "7")
    assert ruta == ["0", "1", "8", "6", "7"]
    assert minutos == 21


def test_origen_igual_destino():
    grafo = cargar_grafo(RAIZ / "datos" / "alto_magdalena.csv")
    ruta, minutos = ruta_mas_rapida(grafo, "0", "0")
    assert ruta == ["0"]
    assert minutos == 0


def test_destino_inalcanzable():
    grafo = Grafo()
    grafo.agregar_vertice("A", "A")
    grafo.agregar_vertice("B", "B")
    assert reconstruir_ruta({"A": None, "B": None}, "A", "B") is None


def test_rechaza_peso_no_positivo():
    grafo = Grafo()
    grafo.agregar_vertice("A", "A")
    grafo.agregar_vertice("B", "B")
    with pytest.raises(ValueError):
        grafo.agregar_arista("A", "B", 0)
