import numpy as np
from matplotlib import pyplot as plt
import random


def generate_random_list(length=500, min_value=1, max_value=1000):
    # Генеруємо випадковий список чисел
    return " ".join(str(random.randint(min_value, max_value)) for _ in range(length))


plt.figure(figsize=(5, 2.7), layout="constrained")
plt.plot(x, y)
plt.xlabel("x label")
plt.ylabel("y label")

plt.savefig("plot.png")  # Зберігає графік у файл
