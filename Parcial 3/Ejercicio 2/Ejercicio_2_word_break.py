class Solution:
    # Programación dinámica:
    # dp[i] indica si el prefijo s[0:i] puede segmentarse
    # usando palabras del diccionario.
    # Recurrencia:
    # dp[i] = True si existe j < i tal que dp[j] es True
    # y s[j:i] está en wordDict.
    # Tiempo: O(n^2)
    # Espacio: O(n)
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]