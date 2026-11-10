"""Algoritmos de rutas sobre el grafo del proyecto."""

from __future__ import annotations

from .estructuras import MonticuloMin
from .grafo import Grafo


def dijkstra(grafo: Grafo, origen: str) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula distancias mínimas desde el origen usando el montículo propio."""
    origen = grafo.resolver_vertice(origen)
    dist = {v: float("inf") for v in grafo.vertices()}
    prev: dict[str, str | None] = {v: None for v in grafo.vertices()}
    dist[origen] = 0.0
    pendientes = MonticuloMin()
    pendientes.insertar(0.0, origen)

    while pendientes:
        distancia, u = pendientes.extraer()
        if distancia != dist[u]:  # descarta entradas antiguas del montículo
            continue
        for v, peso in grafo.vecinos(u):
            alternativa = distancia + peso
            if alternativa < dist[v]:
                dist[v] = alternativa
                prev[v] = u
                pendientes.insertar(alternativa, v)
    return dist, prev


def reconstruir_ruta(
    prev: dict[str, str | None], origen: str, destino: str
) -> list[str] | None:
    """Devuelve IDs de origen a destino, o None si no existe una ruta."""
    if origen not in prev or destino not in prev:
        raise KeyError("El origen y el destino deben pertenecer al grafo")
    ruta: list[str] = []
    actual: str | None = destino
    while actual is not None:
        ruta.append(actual)
        if actual == origen:
            ruta.reverse()
            return ruta
        actual = prev[actual]
    return None


def ruta_mas_rapida(grafo: Grafo, origen: str, destino: str) -> tuple[list[str] | None, float]:
    """Atajo que retorna la ruta y su tiempo total en minutos."""
    origen_id = grafo.resolver_vertice(origen)
    destino_id = grafo.resolver_vertice(destino)
    dist, prev = dijkstra(grafo, origen_id)
    return reconstruir_ruta(prev, origen_id, destino_id), dist[destino_id]
