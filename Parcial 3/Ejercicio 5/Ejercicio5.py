from typing import List
# Programación dinámica (Subset Sum):
    # dp[i] indica si es posible formar una suma i
    # usando algunos elementos del arreglo.
    #
    # Primero se calcula la suma total del arreglo.
    # Si la suma es impar, no se puede dividir en dos subconjuntos iguales.
    #
    # Si es par, el problema se reduce a encontrar un subconjunto
    # que sume total // 2.
    #
    # Recurrencia:
    # dp[i] = dp[i] or dp[i - num]
    # (si puedo formar i - num, entonces puedo formar i agregando num)
    #
    # Se recorre de derecha a izquierda para no reutilizar el mismo elemento.
    #
    # Tiempo: O(n * target)
    # Espacio: O(target)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]

# =========================
# 🔽 PRUEBAS
# =========================
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        [1, 5, 11, 5],
        [1, 2, 3, 5],
        [2, 2, 1, 1],
        [3, 3, 3, 4, 5],
    ]
    
    for nums in test_cases:
        result = sol.canPartition(nums)
        print(f"nums = {nums} -> {result}")