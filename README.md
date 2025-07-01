# Solución de una ecuación diferencial separable con el método de Euler

Este repositorio contiene un ejemplo de resolución de la ecuación diferencial separable:

dy/dt = y

## Solución analítica

La ecuación es separable y su solución exacta, usando separación de variables, es:

y(t) = y₀ * exp(t)

## Solución numérica: Método de Euler

Se utiliza el método de Euler para aproximar la solución en el intervalo t ∈ [0,1] con un paso h = 0.2.

## Archivos
- `metodo_euler.py`: Código Python que resuelve la ecuación analíticamente y numéricamente, y grafica ambas soluciones.

## Ejecución

Asegúrate de tener instaladas las librerías necesarias:

```bash
pip install numpy matplotlib
```

Luego ejecuta:

```bash
python metodo_euler.py
```

Se mostrará una gráfica comparando la solución exacta y la aproximación de Euler.
