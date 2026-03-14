from typing import List

class Solution:
    # Estrategia greedy:
    # Se ordenan los intervalos por su inicio.
    # Luego se recorre la lista una sola vez:
    # - Si el intervalo actual se solapa con el último fusionado, se combinan.
    # - Si no se solapan, se agrega como un nuevo intervalo.
    #
    # Complejidad:
    # Tiempo: O(n log n), por el ordenamiento.
    # Espacio: O(n), por la lista de resultado.

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        return merged