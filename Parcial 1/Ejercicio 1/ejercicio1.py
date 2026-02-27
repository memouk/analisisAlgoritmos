import time
# ============================================================
# SOLUCIÓN 1: Fuerza Bruta
# Complejidad:
#   - Tiempo: O(n^2)
#   - Espacio: O(n)

# Cómo lo hice:
#   - Primero verifico que ambas cadenas tengan la misma longitud.
#   - Convierto la segunda cadena en lista para poder eliminar letras.
#   - Recorro cada carácter de la primera cadena.
#   - Si el carácter existe en la lista, lo elimino (simulando que uso esa letra).
#   - Si no lo encuentro en algún momento, retorno False.
#   - Si termino el recorrido completo sin errores, son anagramas.
# ============================================================
def is_anagram_brute(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    t_list = list(t)
    for char in s:
        if char in t_list:
            t_list.remove(char)
        else:
            return False
    return True

# ============================================================
# SOLUCIÓN 2: Óptima
# Complejidad:
#   - Tiempo: O(n)
#   - Espacio: O(1) si el alfabeto es fijo (ej: solo minúsculas)
#              O(n) en caso general
# Cómo lo hice:
#   - Primero verifico que ambas cadenas tengan la misma longitud.
#   - Uso un diccionario para contar cuántas veces aparece cada letra en s.
#   - Luego recorro la cadena t:
#       - Si aparece una letra que no estaba en s, retorno False.
#       - Resto 1 al contador de esa letra.
#       - Si el contador queda negativo, significa que t tiene más letras
#         de esa que s, entonces retorno False.
#   - Si todo termina correctamente, las cadenas son anagramas.
# ============================================================
def is_anagram_optimized(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    return True
# ============================================================
# PRUEBAS
# ============================================================
if __name__ == "__main__":
    test_cases = [
        ("anagram", "nagaram"),
        ("rat", "car"),
        ("listen", "silent"),
        ("hello", "bello"),
        ("a" * 10000, "a" * 10000),  # caso grande
    ]
    print("============== RESULTADOS ==============\n")

    for s, t in test_cases:
        print(f"Probando: s='{s[:20]}' t='{t[:20]}'")
        # ----------- Fuerza Bruta -----------
        start = time.time()
        result_brute = is_anagram_brute(s, t)
        end = time.time()
        brute_time = end - start
        # ----------- Optimizado -----------
        start = time.time()
        result_opt = is_anagram_optimized(s, t)
        end = time.time()
        opt_time = end - start

        print(f"Fuerza Bruta: {result_brute} | Tiempo: {brute_time:.6f} segundos")
        print(f"Optimizado:   {result_opt} | Tiempo: {opt_time:.6f} segundos")
        print("-" * 50)

    print("\n============= FIN =============")