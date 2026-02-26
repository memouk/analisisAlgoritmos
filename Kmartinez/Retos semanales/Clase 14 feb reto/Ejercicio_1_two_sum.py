from typing import List

class Solution1:
  # ============================================================
  # SOLUCIÓN 1: Fuerza bruta (simple / forzada)
  # Complejidad:
  #   - Tiempo: O(n^2)
  #   - Espacio: O(1)
  #
  # Cómo lo hice:
  #   - Pruebo todas las parejas (i, j) con i < j.
  #   - Si nums[i] + nums[j] == target, retorno [i, j].
  # ============================================================
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
      for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
          return [i, j]
    return []

class Solution2:
  # ============================================================
  # SOLUCIÓN 2: Óptima (Hash map / diccionario)
  # Complejidad:
  #   - Tiempo: O(n) en promedio (búsqueda/insert en dict es O(1) promedio)
  #   - Espacio: O(n)
  #
  # Cómo lo hice:
  #   - Recorro la lista y guardo en un dict: valor -> índice.
  #   - Para cada x, calculo complement = target - x y reviso si ya existe.
  #   - Si existe, retorno [índice_del_complemento, índice_actual].
  # ============================================================
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}

    for i, x in enumerate(nums):
      complement = target - x
      if complement in seen:
        return [seen[complement], i]
      seen[x] = i

    return []
