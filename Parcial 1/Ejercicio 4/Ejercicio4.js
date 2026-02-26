
//  ==========================================================
//  SOLUCIÓN 1: Fuerza bruta
//  Complejidad:
//  - Tiempo: O(n · 2 ^ n)
//  - Espacio: O(n)
//  Cómo lo hice:
//  - Para cada piedra pruebo dos opciones: mantenerla o eliminarla.
//  - Genero todas las combinaciones posibles(2 ^ n subconjuntos).
//  - Para cada combinación verifico si no hay colores iguales consecutivos.
//  - Calculo cuántas piedras fueron eliminadas.
//  - Me quedo con el mínimo número de eliminaciones válidas.
//  Nota: El juez de codeforces obligaba a escribir sintaxis un poco vieja
//  por esto es que no se usa let ni const
//  Ademas de esto la fuerza bruta excede los limites que me pone codeforce
//  Intenté buscar otras soluciones pero ya me estaba inclinando mas por fuerza bruta entonces por eso lo dejé así
//  ==========================================================


function isValid(arr) {
    for (var i = 1; i < arr.length; i++) {
        if (arr[i] === arr[i - 1]) {
            return false;
        }
    }
    return true;
}

function bruteForce(n, s) {
    var minRemoved = n;

    function backtrack(index, current) {
        if (index === n) {
            if (isValid(current)) {
                var removed = n - current.length;
                if (removed < minRemoved) {
                    minRemoved = removed;
                }
            }
            return;
        }

        // Mantener piedra
        backtrack(index + 1, current + s[index]);

        // Eliminar piedra
        backtrack(index + 1, current);
    }

    backtrack(0, "");
    return minRemoved;
}

var n = parseInt(readline());
var s = readline();



// ==========================================================
// SOLUCIÓN 2: Algoritmo óptimo(Greedy)
// Complejidad:
// - Tiempo: O(n)
// - Espacio: O(1)
// Cómo lo hice:
// - Recorro la cadena una sola vez.
// - Comparo cada piedra con la anterior.
// - Si dos piedras consecutivas tienen el mismo color, incremento el contador.
// - El contador representa el número mínimo de piedras a eliminar.
// - Devuelvo ese total como resultado final.
// ==========================================================

var n = parseInt(readline());
var s = readline();

var count = 0;

for (var i = 1; i < n; i++) {
    if (s[i] === s[i - 1]) {
        count++;
    }
}

print(count);