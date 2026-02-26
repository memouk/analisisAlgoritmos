class Solution1:
  # ============================================================
  # SOLUCIÓN 1: Fuerza bruta
  # Complejidad:
  #   - Tiempo: O(n^2)
  #   - Espacio: O(1)
  #
  # Ejecución:
  #   - Para cada inicio i, extiendo el subarreglo hasta "j" acumulando suma.
  #   - Actualizo el máximo global en cada extensión.
  # ============================================================
  def maxSubArray(self, nums):
    best = nums[0]
    n = len(nums)

    for i in range(n):
      current_sum = 0
      for j in range(i, n):
        current_sum += nums[j]
        if current_sum > best:
          best = current_sum

    return best

class Solution2:
  # ============================================================
  # SOLUCIÓN 2: Óptima (Kadane)
  # Complejidad:
  #   - Tiempo: O(n)
  #   - Espacio: O(1)
  #
  # Ejecución:
  #   - current = mejor suma de subarreglo que termina en i.
  #   - current = max(nums[i], current + nums[i])
  #   - best = máximo global.
  # ============================================================
  def maxSubArray(self, nums):
    best = nums[0]
    current = nums[0]

    for i in range(1, len(nums)):
      x = nums[i]
      # current = max(x, current + x) sin usar max()
      if current + x < x:
        current = x
      else:
        current = current + x

      if current > best:
        best = current

    return best