function canJump(nums: number[]): boolean {
    let maxDistance = 0;

    for (let i = 0; i < nums.length; i++) {
        if (i > maxDistance) {
            return false;
        }
        maxDistance = Math.max(maxDistance, i + nums[i]);
    }

    return true;
};

//Ejercicio 55. Jump Game leetCode
/* 
Nos dan un arreglo que contiene numero y lo que nos dicen es que cada
numero nos indica cuantas posiciciones podemos saltar desde alli
Lo ue debemos hacer es devolver un true si podemos llegar a la posicion final o
false si no, ejm

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: desde la posicion 0 podemos saltar a la 1 o la 2,
si saltamos a la 1, luego podremos saltar 3 posiciones y llegar al final, true
si saltamo a la 2 podremos saltar a la 3 y desde la saltar a al final, true

Lo que hacemos es rastrear donde estamos y hasta donde podemos llegar, para esto creamos una variable
llamada maxDistance, asi controlamos a donde podemos llegar, si en algun momento notamos que la posicion
supera al maximo que podemos alcanzar retornamos un false porqiue nos pasamos, sino retornaos un true

Complejidad
Tiempo: O(n) hay un solo loop
Espacio O(1)

*/