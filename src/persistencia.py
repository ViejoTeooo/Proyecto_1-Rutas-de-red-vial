"""Carga y validación de la red vial desde un archivo CSV."""

import csv
from pathlib import Path

from .grafo import Grafo

COLUMNAS = {
    "origen_id", "origen_nombre", "origen_ubicacion",
    "destino_id", "destino_nombre", "destino_ubicacion", "tiempo_min",
}


def cargar_grafo(ruta_archivo: str | Path) -> Grafo:
    ruta = Path(ruta_archivo)
    grafo = Grafo()
    with ruta.open("r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames is None or not COLUMNAS.issubset(lector.fieldnames):
            faltantes = COLUMNAS - set(lector.fieldnames or [])
            raise ValueError(f"Faltan columnas requeridas en el CSV: {', '.join(sorted(faltantes))}")
        filas = list(lector)

    for numero, fila in enumerate(filas, start=2):
        try:
            grafo.agregar_vertice(fila["origen_id"], fila["origen_nombre"], fila["origen_ubicacion"])
            grafo.agregar_vertice(fila["destino_id"], fila["destino_nombre"], fila["destino_ubicacion"])
            grafo.agregar_arista(fila["origen_id"], fila["destino_id"], float(fila["tiempo_min"]))
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"Error en la fila {numero} del CSV: {exc}") from exc
    return grafo
