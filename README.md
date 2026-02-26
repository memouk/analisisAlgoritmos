# 📘 Análisis de Algoritmos — Parciales y Actividades

Repositorio académico para almacenar y versionar **parciales, ejercicios, soluciones (fuerza bruta/óptima)** y material de apoyo de la materia **Análisis de Algoritmos**.


## 👥 Integrantes

> Grupo de 4 estudiantes:

- **Integrante 1:** Luis Felipe Pico Gutiérrez — luispico261741@correo.itm.edu.co
- **Integrante 2:** Luis Guillermo González Ayala — luisgonzalez68694@correo.itm.edu.co
- **Integrante 3:** Yehicol Andrés Hincapie Hoyos — Yehicolhincapie316555@correo.itm.edu.co 
- **Integrante 4:** Kevin Santiago Martinez Molina — kevinmartinez214003@correo.itm.edu.co

## 🎯 Objetivo del repositorio

- Centralizar entregas de la asignatura en un único repositorio.
- Mantener trazabilidad de cambios (Git) y evidencias por ejercicio.
- Comparar enfoques de solución (p. ej., **fuerza bruta vs. solución óptima**).
- Facilitar la revisión y ejecución del código.


## 🗂️ Estructura del proyecto

La organización sigue el esquema: **Parcial → Ejercicios → Código + Evidencias**.

Ejemplo basado en la estructura actual:

```
ANALISISALGORITMOS/
└── Parcial 1/
    ├── Ejercicio 1/
    ├── Ejercicio 2/
    │   ├── ejercicio2.py
    │   ├── ejercicio2FuerzaBruta.png
    │   └── ejercicio2Optimo.png
    ├── Ejercicio 3/
    │   ├── Ejercicio3.py
    │   ├── Solución fuerza bruta.png
    │   └── Solución optima.png
    ├── Ejercicio 4/
    └── README.md
```

✅ **Convención recomendada por ejercicio**
- `ejercicioN.py` → implementación principal
- `*_FuerzaBruta.png` / `*_Optimo.png` → evidencia (análisis, diagrama, captura)
- (Opcional) `explicacion.md` → justificación, complejidad, pseudocódigo


## ⚙️ Requisitos

- **Python 3.10+** (recomendado)

Verifica tu versión:

```bash
python --version
```


## ▶️ Ejecución

Ubícate en la carpeta del ejercicio y ejecuta el archivo:

```bash
cd "Parcial 1/Ejercicio 2"
python ejercicio2.py
```

Si usas `python3`:

```bash
python3 ejercicio2.py
```


## 📦 Entregables por ejercicio (guía)

En cada ejercicio se recomienda incluir:

1. **Descripción del problema** (breve).
2. **Estrategia / enfoque**:
   - Fuerza bruta (si aplica)
   - Optimización (DP, Greedy, Divide & Conquer, etc.)
3. **Complejidad computacional**:
   - Tiempo: `O(...)`
   - Memoria: `O(...)`
4. **Evidencias**:
   - Capturas o diagramas en `.png`
5. **Código ejecutable** (`.py`) con entradas/salidas claras.

## ✅ Estándares mínimos de código

- Nombres descriptivos en variables/funciones.
- Comentarios solo donde agreguen valor (no redundantes).
- Evitar “magic numbers” (usar constantes cuando tenga sentido).
- Separar lógica en funciones para facilitar pruebas y lectura.

---

## 🔁 Flujo de trabajo con Git (simple)

1. Crear/actualizar archivos del ejercicio.
2. `git add .`
3. `git commit -m "Parcial 1: solución Ejercicio 2 (FB y óptima)"`
4. `git push`

> Recomendación: un commit por ejercicio o por mejora relevante.


## 🧩 Fuente de retos (LeetCode)

Los ejercicios y retos prácticos de este repositorio se basan en problemas de **LeetCode** para fortalecer:
- Análisis de complejidad (tiempo/memoria)
- Diseño de algoritmos (DP, Greedy, Divide & Conquer, Graphs, etc.)
- Comparación de enfoques (Fuerza bruta vs. Optimización)


## 📌 Estado (✅/🟡/❌)
- Parcial 1: En progreso 🟡


## 📫 Contacto

- Docente: 
ALEJANDRO SALGAR MARÍN
- Universidad/Institución: alejandrosalgar2487@correo.itm.edu.co