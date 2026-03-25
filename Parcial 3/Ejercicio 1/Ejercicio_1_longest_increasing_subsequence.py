class Solution:
    # Programación dinámica:
    # dp[i] representa la longitud de la subsecuencia creciente
    # más larga que termina exactamente en la posición i.
    # Recurrencia:
    # dp[i] = max(dp[j] + 1) para todo j < i con nums[j] < nums[i]
    # Tiempo: O(n^2)
    # Espacio: O(n)
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)