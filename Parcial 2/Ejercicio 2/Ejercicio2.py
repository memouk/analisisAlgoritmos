"""
Ejercicio 2: Non-overlapping Intervals (LeetCode 435)

Link del problema:
https://leetcode.com/problems/non-overlapping-intervals/

Descripción:
Se tiene un arreglo de intervalos donde:

intervals[i] = [start_i, end_i]

Dos intervalos se solapan si comparten algún punto

Objetivo:
Devolver el número mínimo de intervalos que hay que eliminar
para que los intervalos restantes no se solapen
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            if start < end:
                count += 1 
            else:
                end = intervals[i][1]
        return count
"""
ESTRATEGIA GREEDY

La estrategia voraz consiste en seleccionar siempre el intervalo
que termina primero.

Para ello:

1. Se ordenan los intervalos según su tiempo de finalización.
2. Se mantiene el intervalo que termina más temprano.
3. Si el siguiente intervalo empieza antes de que termine el actual,
   significa que hay solapamiento y se elimina.
4. Si no se solapan, se actualiza el final del intervalo actual.

Este enfoque permite mantener el mayor número posible de intervalos
sin solapamientos.

JUSTIFICACIÓN DEL ENFOQUE GREEDY

Elegir siempre el intervalo que termina primero deja más espacio
disponible para los intervalos siguientes.

Si se eligiera un intervalo que termina más tarde, podría impedir
incluir varios intervalos que empiezan antes.

Por lo tanto, seleccionar siempre el intervalo con menor tiempo
de finalización garantiza maximizar la cantidad de intervalos
no solapados y, en consecuencia, minimizar los que deben eliminarse.

COMPLEJIDAD

Complejidad temporal:

Ordenar los intervalos domina el tiempo de ejecución:

O(n log n)

El recorrido del arreglo es lineal:

O(n)

Complejidad total:

O(n log n)

Complejidad espacial:

O(1)

Solo se utilizan variables auxiliares constantes.
"""
# PRUEBAS LOCALES
if __name__ == "__main__":

    solucion = Solution()

    intervals1 = [[1,2],[2,3],[3,4],[1,3]]
    print("Intervalos:", intervals1)
    print("Intervalos a eliminar:", solucion.eraseOverlapIntervals(intervals1))
    print()

    intervals2 = [[1,2],[1,2],[1,2]]
    print("Intervalos:", intervals2)
    print("Intervalos a eliminar:", solucion.eraseOverlapIntervals(intervals2))
    print()

    intervals3 = [[1,2],[2,3]]
    print("Intervalos:", intervals3)
    print("Intervalos a eliminar:", solucion.eraseOverlapIntervals(intervals3))