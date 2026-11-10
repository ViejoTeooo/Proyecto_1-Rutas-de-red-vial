"""Interfaz de consola para consultar rutas de menor tiempo."""

import argparse
from pathlib import Path

from .algoritmos import ruta_mas_rapida
from .persistencia import cargar_grafo


def main() -> int:
    raiz = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description="Busca rutas de menor tiempo en el Alto Magdalena")
    parser.add_argument("--archivo", default=str(raiz / "datos" / "alto_magdalena.csv"), help="Ruta al CSV de la red vial")
    parser.add_argument("--origen", help="ID o nombre del punto de partida")
    parser.add_argument("--destino", help="ID o nombre del punto de llegada")
    args = parser.parse_args()

    try:
        grafo = cargar_grafo(args.archivo)
        origen = args.origen or input("Origen (ID o nombre): ").strip()
        destino = args.destino or input("Destino (ID o nombre): ").strip()
        ruta, minutos = ruta_mas_rapida(grafo, origen, destino)
        if ruta is None:
            print("No existe una ruta dirigida entre esos puntos.")
            return 1
        nombres = [grafo.vertices_por_id[v].nombre for v in ruta]
        print("\nRuta de menor tiempo:")
        print(" → ".join(nombres))
        print(f"Tiempo total: {minutos:g} minutos")
        return 0
    except (OSError, ValueError, KeyError) as exc:
        parser.error(str(exc))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
