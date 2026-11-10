"""Grafo dirigido ponderado representado con listas de adyacencia."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Vertice:
    identificador: str
    nombre: str
    ubicacion: str = ""


class Grafo:
    """Cada arista (u, v, peso) representa viaje permitido de u hacia v."""

    def __init__(self) -> None:
        self.vertices_por_id: dict[str, Vertice] = {}
        self._nombres: dict[str, str] = {}
        self.adj: dict[str, list[tuple[str, float]]] = {}

    def agregar_vertice(self, identificador: str, nombre: str, ubicacion: str = "") -> None:
        identificador = str(identificador).strip()
        nombre = nombre.strip()
        if not identificador or not nombre:
            raise ValueError("El identificador y el nombre del vértice son obligatorios")
        previo = self.vertices_por_id.get(identificador)
        vertice = Vertice(identificador, nombre, ubicacion.strip())
        if previo and previo.nombre != nombre:
            raise ValueError(f"El identificador {identificador} tiene nombres incompatibles")
        otro_id = self._nombres.get(nombre.casefold())
        if otro_id is not None and otro_id != identificador:
            raise ValueError(f"El nombre {nombre!r} está asociado a más de un identificador")
        self.vertices_por_id[identificador] = vertice
        self._nombres[nombre.casefold()] = identificador
        self.adj.setdefault(identificador, [])

    def agregar_arista(self, origen: str, destino: str, peso: float) -> None:
        origen, destino = str(origen).strip(), str(destino).strip()
        peso = float(peso)
        if peso <= 0:
            raise ValueError("El tiempo de recorrido debe ser mayor que cero")
        if origen not in self.adj or destino not in self.adj:
            raise KeyError("Primero deben registrarse los dos vértices de la arista")
        if any(vecino == destino for vecino, _ in self.adj[origen]):
            raise ValueError(f"La conexión {origen} → {destino} está duplicada")
        self.adj[origen].append((destino, peso))

    def vecinos(self, identificador: str) -> list[tuple[str, float]]:
        try:
            return list(self.adj[str(identificador)])
        except KeyError as exc:
            raise KeyError(f"No existe el vértice {identificador!r}") from exc

    def resolver_vertice(self, valor: str) -> str:
        valor = str(valor).strip()
        if valor in self.vertices_por_id:
            return valor
        identificador = self._nombres.get(valor.casefold())
        if identificador is None:
            raise KeyError(f"No se encontró un vértice con ID o nombre {valor!r}")
        return identificador

    def vertices(self) -> list[str]:
        return list(self.vertices_por_id)

    def cantidad_aristas(self) -> int:
        return sum(map(len, self.adj.values()))
