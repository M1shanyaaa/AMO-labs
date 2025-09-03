import flet as ft
import os
import numpy as np
import matplotlib.pyplot as plt


def selection_sort(arr):
    n = len(arr)
    operations = 0
    for min_index in range(n - 1):
        least = min_index
        for j in range(min_index + 1, n):
            operations += 1
            if arr[j] < arr[least]:
                least = j
        arr[min_index], arr[least] = arr[least], arr[min_index]
    return arr, operations


def read_file():
    file_path = "list_for_sort"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                return list(map(int, file.read().split()))
            except ValueError:
                return None
    return None


def measure_operations():
    sizes = np.linspace(10, 4000, 10, dtype=int)
    operations_count = []
    theoretical_complexity = []

    for size in sizes:
        arr = np.random.randint(0, 100000, size).tolist()
        _, operations = selection_sort(arr)
        operations_count.append(operations)
        theoretical_complexity.append(size**2)

    return sizes, operations_count, theoretical_complexity


def make_graph(e, graph_container, page):
    sizes, operations_count, theoretical_complexity = measure_operations()

    plt.figure(figsize=(8, 5))
    plt.plot(sizes, operations_count, label="Кількість операцій", marker="o")
    plt.plot(
        sizes, theoretical_complexity, label="Відносна складність O(n²)", linestyle="--"
    )
    plt.xlabel("Розмір масиву")
    plt.ylabel("Кількість операцій")
    plt.legend()
    plt.title("Порівняння кількості операцій та відносної складності")
    plt.grid()

    graph_path = "operations_vs_size_plot.png"
    plt.savefig(graph_path)
    plt.close()

    img = ft.Image(src=graph_path, width=600, height=400)
    graph_container.controls.clear()
    graph_container.controls.append(img)
    page.update()


def main(page: ft.Page):
    page.bgcolor = "white"
    page.theme = ft.Theme(color_scheme_seed="black")
    page.title = "Сортування вибором"

    input_field = ft.TextField(
        label="Введіть числа через пробіл", bgcolor="white", color="black"
    )
    result_text = ft.Text("Результат сортування: ", bgcolor="white", color="black")

    graph_container = ft.Column()

    def on_sort(e):
        try:
            numbers = list(map(int, input_field.value.split()))
            sorted_numbers, _ = selection_sort(numbers)
            result_text.value = f"Результат сортування: {sorted_numbers}"
            make_graph(e, graph_container, page)
        except ValueError:
            result_text.value = "Помилка: введіть коректні числа"
        page.update()

    def on_sort_file(e):
        numbers = read_file()
        if numbers is not None:
            sorted_numbers, _ = selection_sort(numbers)
            result_text.value = f"Результат сортування: {sorted_numbers}"
            make_graph(e, graph_container, page)
        else:
            result_text.value = "Помилка: не вдалося прочитати файл"
        page.update()

    main_tab = ft.Column(
        [
            ft.Text("Програма сортування вибором", bgcolor="white", color="black"),
            input_field,
            ft.ElevatedButton(
                "Сортувати", on_click=on_sort, bgcolor="white", color="black"
            ),
            ft.ElevatedButton(
                "Сортувати з файлу",
                on_click=on_sort_file,
                bgcolor="white",
                color="black",
            ),
            result_text,
        ]
    )

    algorithm_tab = ft.Column(
        [
            ft.Text(
                "Автор: \n   Рибачок Михайло Володимирович \n   ІО-34 Варіант 17 \n  Лабораторна робота №2",
                size=24,
                weight=ft.FontWeight.BOLD,
                color="black",
            ),
        ]
    )

    graph_of_algorithm = ft.Column([graph_container])

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Головна", content=algorithm_tab),
            ft.Tab(text="Алгоритм", content=main_tab),
            ft.Tab(text="Графіки складності", content=graph_of_algorithm),
        ],
    )

    page.add(tabs)


ft.app(target=main)
