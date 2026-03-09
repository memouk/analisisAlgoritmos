"""
Ejercicio 1: Assign Cookies (LeetCode 455)

Link del problema:
https://leetcode.com/problems/assign-cookies/

Descripción:
Se tiene un arreglo g donde g[i] representa el nivel de avaricia del niño i
(es decir, el tamaño mínimo de galleta que acepta).

Se tiene otro arreglo s donde s[j] representa el tamaño de la galleta j.

Reglas:
- Cada niño puede recibir como máximo una galleta.
- Una galleta j puede asignarse a un niño i solo si:
        s[j] >= g[i]

Objetivo:
Maximizar el número de niños satisfechos.
"""

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1 
            j += 1
        return i
"""
ESTRATEGIA GREEDY

La estrategia voraz consiste en asignar la galleta más pequeña posible
al niño menos exigente.

1. Se ordenan los niños según su nivel de avaricia.
2. Se ordenan las galletas según su tamaño.
3. Se usan dos punteros para recorrer ambos arreglo

Si una galleta puede satisfacer al niño actual, se asigna y se pasa al
siguiente niño

Siempre se avanza en las galletas para intentar satisfacer al mayor
número posible de niños

JUSTIFICACIÓN DEL ENFOQUE GREEDY

Asignar primero las galletas más pequeñas a los niños menos exigentes
evita desperdiciar galletas grandes en niños que podrían aceptar una
más pequeña

Si se utilizara una galleta grande para un niño con baja avaricia,
podría impedir satisfacer a un niño más exigente más adelante

Por lo tanto, elegir siempre la galleta mínima suficiente para el
niño actual es una decisión local que conduce a una solución óptima
global

COMPLEJIDAD

Complejidad temporal:

Ordenar los arreglos domina el tiempo de ejecución:

O(n log n + m log m)

donde:
n = número de niños
m = número de galletas

El recorrido con los dos punteros es lineal:

O(n + m)

Complejidad espacial:

O(1)

Solo se utilizan variables auxiliares constantes.
"""
# -------------------------
# PRUEBA DEL ALGORITMO
# -------------------------

if __name__ == "__main__":
    
    solucion = Solution()
    # Ejemplo 1 del problema
    g = [1, 2, 3]
    s = [1, 1]

    resultado = solucion.findContentChildren(g, s)

    print("Niños:", g)
    print("Galletas:", s)
    print("Niños satisfechos:", resultado)