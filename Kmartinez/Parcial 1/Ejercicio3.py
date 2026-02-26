from typing import List

class Solution1:
  # ============================================================
  # SOLUCIÓN 1: Fuerza bruta
  # Complejidad:
  #   - Tiempo: O(n^2)
  #   - Espacio: O(1)
  #
  # Cómo lo hice:
  #   - Pruebo todas las parejas (i, j) con i < j.
  #   - Ganancia = prices[j] - prices[i].
  #   - Me quedo con la mayor ganancia encontrada.
  #   - Si no hay ganancia posible, retorno 0.
  # ============================================================
  def maxProfit(self, prices: List[int]) -> int:
    best = 0
    n = len(prices)

    for i in range(n):
      for j in range(i + 1, n):
        profit = prices[j] - prices[i]
        if profit > best:
          best = profit

    return best

class Solution2:
  # ============================================================
  # SOLUCIÓN 2: Óptima
  # Complejidad:
  #   - Tiempo: O(n)
  #   - Espacio: O(1)
  #
  # Cómo lo hice:
  #   - Mantengo min_price = el menor precio visto hasta el momento.
  #   - Para cada precio p:
  #       best = max(best, p - min_price)  (vender hoy si conviene)
  #       min_price = min(min_price, p)   (mejor día para comprar hasta hoy)
  #   - Así garantizo comprar antes de vender y obtengo la mejor ganancia.
  # ============================================================
  def maxProfit(self, prices: List[int]) -> int:
    min_price = prices[0]
    best = 0

    for p in prices[1:]:
      best = max(best, p - min_price)
      min_price = min(min_price, p)

    return best