"""Medición orientativa de Dijkstra con grafos sintéticos dispersos."""

from time import perf_counter

from src.algoritmos import dijkstra
from src.grafo import Grafo


def crear_grafo(cantidad: int) -> Grafo:
    grafo = Grafo()
    for i in range(cantidad):
        grafo.agregar_vertice(str(i), f"Nodo {i}")
    # Cadena conectada más algunos atajos para simular una red dispersa.
    for i in range(cantidad - 1):
        grafo.agregar_arista(str(i), str(i + 1), 1 + (i % 7))
    for i in range(0, cantidad - 3, 4):
        grafo.agregar_arista(str(i), str(i + 3), 5)
    return grafo


def main() -> None:
    print("nodos,aristas,tiempo_segundos")
    for cantidad in (100, 500, 1000, 2500, 5000):
        grafo = crear_grafo(cantidad)
        inicio = perf_counter()
        dijkstra(grafo, "0")
        duracion = perf_counter() - inicio
        print(f"{cantidad},{grafo.cantidad_aristas()},{duracion:.6f}")


if __name__ == "__main__":
    main()
