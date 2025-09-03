import time
from random import randint
import threading


# Функція підрахунку суми
def calculate_sum(lst):
    total = 0
    for item in lst:
        total += item
    return total


# Сума без багатопоточності
N = 30_000_000
numbers = [randint(0, 100) for _ in range(N)]

timer0 = time.time()
total_sum = calculate_sum(numbers)  # Використовуємо змінну total_sum
timer1 = time.time()
print(f"Сума без потоків: {total_sum}, Час: {timer1 - timer0:.4f} сек.")


# Сума з багатопоточністю
def partial_sum(start, end, result_list, index):
    """Функція для підрахунку суми підмасиву"""
    result_list[index] = sum(numbers[start:end])  # Використовуємо оригінальну sum


# Ділення масиву на 4 частини
num_threads = 4
chunk_size = N // num_threads
threads = []
results = [0] * num_threads  # Тут зберігаємо результати потоків

start_time = time.time()

for i in range(num_threads):
    start_index = i * chunk_size
    end_index = N if i == num_threads - 1 else (i + 1) * chunk_size
    thread = threading.Thread(
        target=partial_sum, args=(start_index, end_index, results, i)
    )
    threads.append(thread)
    thread.start()

# Чекаємо завершення всіх потоків
for thread in threads:
    thread.join()

total_sum_threads = sum(results)  # Об'єднуємо результати потоків
end_time = time.time()

print(f"Сума з потоками: {total_sum_threads}, Час: {end_time - start_time:.4f} сек.")
