import flet as ft
import numpy as np
import matplotlib.pyplot as plt
import base64
import io


def aitken_interpolation(x, y, xp):
    n = len(x)
    p = np.copy(y)
    for k in range(1, n):
        for i in range(n - k):
            p[i] = ((xp - x[i + k]) * p[i] + (x[i] - xp) * p[i + 1]) / (x[i] - x[i + k])
    return p[0]


def sin_function(x):
    return np.sin(x)


def sin_squared_function(x):
    return np.sin(x) ** 2


def plot_to_base64():
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode()


def make_graph(
    a,
    b,
    n,
    selected_func,
    graph_container,
    error_graph_container,
    error_table_container,
    page,
):
    try:
        a = float(a)
        b = float(b)
        n = int(n)
        func = sin_function if selected_func == "sin(x)" else sin_squared_function

        x_nodes = np.linspace(a, b, n)
        y_nodes = func(x_nodes)
        x_values = np.linspace(a, b, 100)
        y_theoretical = func(x_values)

        y_interpolated_aitken = np.array(
            [aitken_interpolation(x_nodes, y_nodes, x) for x in x_values]
        )

        # Основний графік
        plt.figure(figsize=(8, 5))
        plt.plot(
            x_values, y_theoretical, label=selected_func, linestyle="--", color="blue"
        )
        plt.plot(
            x_values, y_interpolated_aitken, label="Інтерполяція Ейткена", color="red"
        )
        plt.scatter(x_nodes, y_nodes, color="black", label="Вузли інтерполяції")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.title("Інтерполяція: Теоретична функція vs Інтерполяція Ейткена")
        plt.grid()
        graph_b64 = plot_to_base64()
        plt.close()

        img = ft.Image(src_base64=graph_b64, width=600, height=400)
        graph_container.controls.clear()
        graph_container.controls.append(img)

        # Оновлення сторінки
        page.update()
    except ValueError:
        print("Помилка введення: перевірте, чи правильно введені значення.")


def main(page: ft.Page):
    page.bgcolor = "white"
    page.theme = ft.Theme(color_scheme_seed="black")
    page.title = "Лабораторна робота №3"

    input_field_a = ft.TextField(label="Введіть a", bgcolor="white", color="black")
    input_field_b = ft.TextField(label="Введіть b", bgcolor="white", color="black")
    input_field_n = ft.TextField(label="Введіть n", bgcolor="white", color="black")
    function_selector = ft.Dropdown(
        label="Оберіть функцію",
        options=[ft.dropdown.Option("sin(x)"), ft.dropdown.Option("sin^2(x)")],
        value="sin(x)",
        bgcolor="white",
        color="black",
    )

    graph_container = ft.Column()
    error_graph_container = ft.Column()
    error_table_container = ft.Column()

    main_tab_content = ft.Column(
        controls=[
            ft.Text("Інтерполяція за методом Ейткена", color="black"),
            input_field_a,
            input_field_b,
            input_field_n,
            function_selector,
            ft.ElevatedButton(
                "Вивід графіків",
                on_click=lambda _: make_graph(
                    input_field_a.value,
                    input_field_b.value,
                    input_field_n.value,
                    function_selector.value,
                    graph_container,
                    error_graph_container,
                    error_table_container,
                    page,
                ),
                bgcolor="black",
                color="white",
            ),
            graph_container,
        ],
        scroll=ft.ScrollMode.ALWAYS,
        expand=True,
    )

    main_tab = ft.Container(
        content=ft.Column([main_tab_content], scroll=ft.ScrollMode.AUTO), expand=True
    )

    algorithm_tab = ft.Column(
        [
            ft.Text(
                "Автор: \n Рибачок Михайло Володимирович \n ІО-34 Варіант 17 \n Лабораторна робота 3",
                size=24,
                weight=ft.FontWeight.BOLD,
                color="black",
            ),
        ]
    )

    algorithm = ft.Column([ft.Text(color="black")])

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Головна", content=algorithm_tab),
            ft.Tab(
                text="Інтерполяція виразу за рекурентним співвідношенням Ейткена",
                content=main_tab,
            ),
            ft.Tab(text="Алгоритми", content=algorithm),
        ],
        expand=True,
    )

    page.add(ft.Container(content=tabs, expand=True))


ft.app(target=main)
