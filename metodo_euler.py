"""
Solución de la ecuación diferencial separable dy/dt = y
Solución analítica: y(t) = y0 * exp(t)
Aproximación numérica: Método de Euler
"""
import numpy as np
import matplotlib.pyplot as plt


def solucion_analitica(t, y0):
    return y0 * np.exp(t)

def euler(f, t0, y0, h, n):
    t = [t0]
    y = [y0]
    for i in range(n):
        y_new = y[-1] + h * f(t[-1], y[-1])
        t_new = t[-1] + h
        t.append(t_new)
        y.append(y_new)
    return np.array(t), np.array(y)

def f(t, y):
    return y

# Parámetros iniciales
t0 = 0
y0 = 1
h = 0.2
n = int((1 - t0) / h)

t_euler, y_euler = euler(f, t0, y0, h, n)

t_exacta = np.linspace(t0, 1, 100)
y_exacta = solucion_analitica(t_exacta, y0)

plt.plot(t_exacta, y_exacta, label='Solución exacta', color='blue')
plt.plot(t_euler, y_euler, 'o--', label='Euler', color='red')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Comparación: Solución exacta vs Método de Euler')
plt.legend()
plt.grid()
plt.savefig('metodo_euler.png')
