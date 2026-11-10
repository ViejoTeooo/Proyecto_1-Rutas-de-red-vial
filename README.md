# Rutas óptimas del Alto Magdalena

Proyecto académico en Python para modelar una red vial dirigida y encontrar, mediante el algoritmo de Dijkstra, el recorrido con menor tiempo estimado entre dos puntos. La red se representa con listas de adyacencia y los pesos están expresados en minutos.

## Alcance de esta versión

Esta versión ejecutable contiene los 10 nodos nombrados en el informe y las 10 conexiones dirigidas que pueden leerse explícitamente en su matriz de adyacencia. El informe también menciona 15 aristas, pero la matriz visible solo especifica 10; por eso no se inventan las otras cinco. Antes de presentar resultados como completos, agreguen las conexiones faltantes confirmadas por el equipo o el docente al archivo `datos/alto_magdalena.csv`.

Los tiempos son los valores del ejemplo académico y no representan datos de tráfico en tiempo real. Dijkstra requiere pesos no negativos; esta implementación exige pesos estrictamente positivos, de acuerdo con el modelo del informe.

## Requisitos

- Python 3.11 o superior
- No requiere dependencias externas para ejecutar la aplicación
- Opcional: `pytest` para ejecutar las pruebas

## Ejecución

Desde la carpeta raíz del proyecto:

```bash
python -m src.app
```

Se puede indicar origen y destino como identificadores o como nombres exactos:

```bash
python -m src.app --origen 0 --destino 7
python -m src.app --origen "Parque de Bolívar" --destino "Centro de Agua de Dios"
```

Para elegir otro archivo de datos:

```bash
python -m src.app --archivo datos/alto_magdalena.csv --origen 0 --destino 7
```

## Resultado de referencia

Con los datos incluidos, la ruta desde el Parque de Bolívar hasta el Centro de Agua de Dios es:

`Parque de Bolívar → Sede Unipiloto SAM → Terminal de Transportes → Cruce Agua de Dios → Centro de Agua de Dios`

Tiempo estimado: **21 minutos**.

## Formato de datos

Cada fila de `datos/alto_magdalena.csv` es una arista dirigida y contiene:

`origen_id,origen_nombre,origen_ubicacion,destino_id,destino_nombre,destino_ubicacion,tiempo_min`

Para representar una vía de doble sentido, agreguen dos filas, una por cada sentido. Los identificadores y nombres deben ser consistentes entre filas. El cargador crea los vértices automáticamente y rechaza pesos inválidos.

## Organización

- `src/estructuras.py`: nodo enlazado, pila, cola y montículo mínimo implementados sin `heapq`.
- `src/grafo.py`: grafo dirigido con listas de adyacencia y validación de aristas.
- `src/algoritmos.py`: Dijkstra y reconstrucción de ruta.
- `src/persistencia.py`: carga y validación del CSV.
- `src/app.py`: interfaz de consola.
- `datos/alto_magdalena.csv`: red de ejemplo.
- `tests/`: pruebas automatizadas de estructuras y rutas.
- `rendimiento/medir.py`: medición sencilla del tiempo de Dijkstra en redes sintéticas.

## Ejecutar pruebas

Instalen `pytest` si no está disponible y ejecuten desde la raíz:

```bash
python -m pip install pytest
python -m pytest
```

## Cargar este proyecto en GitHub

Creen un repositorio vacío en GitHub, luego desde esta carpeta:

```bash
git init
git add .
git commit -m "Agregar proyecto de rutas óptimas"
git branch -M main
git remote add origin https://github.com/USUARIO/NOMBRE-REPOSITORIO.git
git push -u origin main
```

Reemplacen `USUARIO` y `NOMBRE-REPOSITORIO` por los valores reales de su cuenta y repositorio.

## Créditos

Proyecto académico de Estructura de Datos, Ingeniería de Sistemas, Universidad Piloto de Colombia, Seccional del Alto Magdalena. Completen aquí los nombres definitivos del equipo y los datos de la asignatura antes de publicar.
