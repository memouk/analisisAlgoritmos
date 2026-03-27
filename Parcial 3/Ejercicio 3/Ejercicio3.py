class Solucion:
    def numDecodings(self, s: str) -> int:
        # Caso base: si la cadena está vacía o empieza en 0, no hay forma válida
        if not s or s[0] == '0':
            return 0
        
        # Variables para optimizar espacio (DP)
        # prev2 = dp[i-2], prev1 = dp[i-1]
        prev2 = 1
        prev1 = 1
        
        for i in range(1, len(s)):
            actual = 0
            
            # Opción 1: tomar solo un dígito
            if s[i] != '0':
                actual += prev1
            
            # Opción 2: tomar dos dígitos
            dos_digitos = int(s[i-1:i+1])
            if 10 <= dos_digitos <= 26:
                actual += prev2
            
            # Actualizamos los valores
            prev2, prev1 = prev1, actual
        
        return prev1



if __name__ == "__main__":
    solucion = Solucion()
    
    casos = [
        ("12", 2),
        ("226", 3),
        ("06", 0),
        ("10", 1),
        ("2101", 1),
        ("11106", 2),
        ("27", 1),
        ("0", 0),
    ]
    
    for cadena, esperado in casos:
        resultado = solucion.numDecodings(cadena)
        print(f"Entrada: {cadena} | Resultado: {resultado} | Esperado: {esperado} | {'OK' if resultado == esperado else 'ERROR'}")