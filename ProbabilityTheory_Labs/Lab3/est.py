import numpy as np
from scipy.integrate import dblquad, quad


# Функція розподілу f(x, y)
def f_xy(x, y):
    if 0 <= x <= 1 and 0 <= y <= 1 - x:
        return 3 * (1 - x - y)
    return 0


# Обчислення часткової функції j(x)
def j_x(x):
    return quad(lambda y: f_xy(x, y), 0, 1 - x)[0]


# Обчислення часткової функції ψ(y)
def psi_y(y):
    return quad(lambda x: f_xy(x, y), 0, 1 - y)[0]


# Математичне сподівання
mx = quad(lambda x: x * j_x(x), 0, 1)[0]
my = quad(lambda y: y * psi_y(y), 0, 1)[0]

# Дисперсія
Dx = quad(lambda x: x**2 * j_x(x), 0, 1)[0] - mx**2
Dy = quad(lambda y: y**2 * psi_y(y), 0, 1)[0] - my**2

# Середньоквадратичне відхилення
sx = np.sqrt(Dx)
sy = np.sqrt(Dy)

# Коваріація
cov_xy = (
    dblquad(lambda x, y: x * y * f_xy(x, y), 0, 1, lambda x: 0, lambda x: 1 - x)[0]
    - mx * my
)

# Коефіцієнт кореляції
r = cov_xy / (sx * sy)

print(f"Математичне сподівання mx: {mx}, my: {my}")
print(f"Середньоквадратичні відхилення sx: {sx}, sy: {sy}")
print(f"Коефіцієнт кореляції r: {r}")
