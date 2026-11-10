import pytest

from src.estructuras import Cola, MonticuloMin, Pila


def test_pila_es_lifo():
    pila = Pila()
    pila.push("A")
    pila.push("B")
    assert pila.peek() == "B"
    assert pila.pop() == "B"
    assert pila.pop() == "A"
    with pytest.raises(IndexError):
        pila.pop()


def test_cola_es_fifo():
    cola = Cola()
    cola.encolar(1)
    cola.encolar(2)
    assert cola.desencolar() == 1
    assert cola.desencolar() == 2
    with pytest.raises(IndexError):
        cola.desencolar()


def test_monticulo_extrae_prioridad_menor():
    monticulo = MonticuloMin()
    monticulo.insertar(5, "cinco")
    monticulo.insertar(2, "dos")
    monticulo.insertar(3, "tres")
    assert [monticulo.extraer()[0] for _ in range(3)] == [2, 3, 5]


def test_monticulo_vacio_lanza_error():
    with pytest.raises(IndexError):
        MonticuloMin().extraer()
