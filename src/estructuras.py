"""Estructuras enlazadas y montículo mínimo implementados desde cero."""

from __future__ import annotations

from typing import Any


class Nodo:
    """Nodo enlazado simple usado por la pila y la cola."""

    def __init__(self, dato: Any, siguiente: Nodo | None = None) -> None:
        self.dato = dato
        self.siguiente = siguiente


class Pila:
    """Pila LIFO con operaciones push, pop y peek en O(1)."""

    def __init__(self) -> None:
        self._tope: Nodo | None = None
        self._cantidad = 0

    def push(self, dato: Any) -> None:
        self._tope = Nodo(dato, self._tope)
        self._cantidad += 1

    def pop(self) -> Any:
        if self._tope is None:
            raise IndexError("No se puede sacar de una pila vacía")
        dato = self._tope.dato
        self._tope = self._tope.siguiente
        self._cantidad -= 1
        return dato

    def peek(self) -> Any:
        if self._tope is None:
            raise IndexError("La pila está vacía")
        return self._tope.dato

    def __len__(self) -> int:
        return self._cantidad

    def __bool__(self) -> bool:
        return self._tope is not None


class Cola:
    """Cola FIFO enlazada con inserción y extracción en O(1)."""

    def __init__(self) -> None:
        self._frente: Nodo | None = None
        self._final: Nodo | None = None
        self._cantidad = 0

    def encolar(self, dato: Any) -> None:
        nuevo = Nodo(dato)
        if self._final is None:
            self._frente = self._final = nuevo
        else:
            self._final.siguiente = nuevo
            self._final = nuevo
        self._cantidad += 1

    def desencolar(self) -> Any:
        if self._frente is None:
            raise IndexError("No se puede desencolar una cola vacía")
        dato = self._frente.dato
        self._frente = self._frente.siguiente
        self._cantidad -= 1
        if self._frente is None:
            self._final = None
        return dato

    def __len__(self) -> int:
        return self._cantidad

    def __bool__(self) -> bool:
        return self._frente is not None


class MonticuloMin:
    """Cola de prioridad binaria mínima, almacenada en una lista."""

    def __init__(self) -> None:
        self._a: list[tuple[float, int, Any]] = []
        self._orden = 0

    def insertar(self, prioridad: float, dato: Any) -> None:
        elemento = (prioridad, self._orden, dato)
        self._orden += 1
        self._a.append(elemento)
        self._subir(len(self._a) - 1)

    def extraer(self) -> tuple[float, Any]:
        if not self._a:
            raise IndexError("No se puede extraer de un montículo vacío")
        minimo = self._a[0]
        ultimo = self._a.pop()
        if self._a:
            self._a[0] = ultimo
            self._bajar(0)
        return minimo[0], minimo[2]

    def _subir(self, indice: int) -> None:
        while indice > 0:
            padre = (indice - 1) // 2
            if self._a[padre] <= self._a[indice]:
                break
            self._a[padre], self._a[indice] = self._a[indice], self._a[padre]
            indice = padre

    def _bajar(self, indice: int) -> None:
        n = len(self._a)
        while True:
            izq, der = 2 * indice + 1, 2 * indice + 2
            menor = indice
            if izq < n and self._a[izq] < self._a[menor]:
                menor = izq
            if der < n and self._a[der] < self._a[menor]:
                menor = der
            if menor == indice:
                return
            self._a[indice], self._a[menor] = self._a[menor], self._a[indice]
            indice = menor

    def __len__(self) -> int:
        return len(self._a)

    def __bool__(self) -> bool:
        return bool(self._a)
