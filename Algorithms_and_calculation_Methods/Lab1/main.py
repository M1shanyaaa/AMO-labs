import flet as ft
import math
import os, ast

linear_dic = {"a": 4, "b": 5}
branching_dic = {"i": 3, "q": 2, "p": 3, "d": 5, "v": 2, "c": 7, "h": 8, "x": 1}
cyclic_dic = {"n": 3, "a": 4, "b": 5}


def main(page: ft.Page):
    page.title = "Редактор алгоритмів"
    page.bgcolor = "#FAE3D9"  # Пастельний фон
    page.theme = ft.Theme(color_scheme_seed="black")  # Чорний текст

    def show_alg(e):
        # Додаємо картинку до існуючого вікна
        page.add(ft.Image(src="images/image.png", width=1200, height=300))
        page.update()

    def write_file(filename, data):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(data))

    def show_main(e):
        page.clean()
        page.add(
            ft.Column(
                [
                    ft.Text(
                        "Автор: \n   Рибачок Михайло Володимирочив \n   ІО-34 Варіант 17",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color="black",
                    ),
                    ft.ElevatedButton(
                        "Лінійний алгоритм",
                        on_click=show_linear,
                        bgcolor="#B5EAD7",
                        color="black",
                    ),
                    ft.ElevatedButton(
                        "Розгалужений алгоритм",
                        on_click=show_branching,
                        bgcolor="#B5EAD7",
                        color="black",
                    ),
                    ft.ElevatedButton(
                        "Циклічний алгоритм",
                        on_click=show_cyclic,
                        bgcolor="#B5EAD7",
                        color="black",
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
        page.update()

    def read_file(filename, default_dic):
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as file:
                file.write(str(default_dic))
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
                try:
                    dic = ast.literal_eval(content)
                    if isinstance(dic, dict):
                        return dic
                except (SyntaxError, ValueError):
                    print(
                        f"Помилка: неможливо перетворити вміст файлу {filename} у словник."
                    )
        return default_dic

    def show_linear(e):
        page.clean()
        a = ft.TextField(label="Введіть a", color="black")
        b = ft.TextField(label="Введіть b", color="black")
        result = ft.Text(color="black")

        def calculate(e):
            try:
                a_value = float(a.value)
                b_value = float(b.value)
                write_file("linear.txt", {"a": a_value, "b": b_value})
                y1 = ((a_value / b_value - 5) / 2) + math.sqrt(
                    (b_value / a_value + 5) / 3
                )
                result.value = f"Результат: {y1:.4f}"
            except Exception as err:
                result.value = f"Помилка: {err}--> Неправельно введені дані, переконайтеся, що не відбувається ділення на нуль чи під кореневий вираз менше за '0' або інше"
            page.update()

        def load_from_file_linear_alg(e):
            data = read_file("linear.txt", linear_dic)
            a.value = str(data["a"])
            b.value = str(data["b"])
            calculate(e)
            page.update()

        # Основне вікно з кнопками
        page.add(
            ft.Column(
                [
                    a,
                    b,
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "Обчислити",
                                on_click=calculate,
                                bgcolor="#FFDAC1",
                                color="black",
                            ),
                            ft.ElevatedButton(
                                "Відобразити алгоритм",
                                on_click=show_alg,
                                bgcolor="#FFDAC1",
                                color="black",
                            ),
                        ]
                    ),
                    ft.ElevatedButton(
                        "Зчитати з файлу",
                        on_click=load_from_file_linear_alg,
                        bgcolor="#FF9AA2",
                        color="black",
                    ),
                    ft.ElevatedButton(
                        "Головне меню",
                        on_click=show_main,
                        bgcolor="#FF9AA2",
                        color="black",
                    ),
                    result,
                ]
            )
        )

        page.update()

    def show_branching(e):
        page.clean()
        fields = {
            name: ft.TextField(label=f"Введіть {name}", color="black")
            for name in branching_dic.keys()
        }
        result = ft.Text(color="black")

        def calculate(e):
            try:
                values = {name: float(field.value) for name, field in fields.items()}
                write_file("branching.txt", values)

                if values["i"] % 3 == 0:
                    y = (values["q"] ** values["i"] * values["d"]) / math.sqrt(
                        values["v"] + values["x"]
                    ) + (values["p"] ** values["i"] * values["d"]) / math.sqrt(
                        values["c"] + values["h"]
                    )
                else:
                    y = (values["v"] * values["d"]) / math.sqrt(
                        values["q"] ** values["i"] + values["x"]
                    ) + (values["c"] * values["d"]) / math.sqrt(
                        values["p"] ** values["i"] + values["h"]
                    )
                result.value = f"Результат: {y:.4f}"
            except Exception as err:
                result.value = f"Помилка: {err}--> Неправельно введені дані, переконайтеся, що не відбувається ділення на нуль чи під кореневий вираз менше за '0' або інше"
            page.update()

        def load_from_file_branching_alg(e):
            data = read_file("branching.txt", branching_dic)
            for name, field in fields.items():
                field.value = str(data[name])
            calculate(e)
            page.update()

        page.add(
            ft.Column(
                list(fields.values())
                + [
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "Обчислити",
                                on_click=calculate,
                                bgcolor="#FFDAC1",
                                color="black",
                            ),
                            ft.ElevatedButton(
                                "Відобразити алгоритм",
                                on_click=show_alg,
                                bgcolor="#FFDAC1",
                                color="black",
                            ),
                        ]
                    ),
                    ft.ElevatedButton(
                        "Зчитати з файлу",
                        on_click=load_from_file_branching_alg,
                        bgcolor="#FF9AA2",
                        color="black",
                    ),
                    ft.ElevatedButton(
                        "Головне меню",
                        on_click=show_main,
                        bgcolor="#FF9AA2",
                        color="black",
                    ),
                    result,
                ]
            )
        )
        page.update()

    def show_cyclic(e):
        page.clean()

        radio_group = ft.RadioGroup(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Radio(value="0"),
                            ft.Text("Перший спосіб обрахунку", color="black"),
                        ]
                    ),
                    ft.Row(
                        [
                            ft.Radio(value="1"),
                            ft.Text("Другий спосіб обрахунку", color="black"),
                        ]
                    ),
                ]
            ),
        )
        page.add(radio_group)

        n = ft.TextField(label="Введіть n (натуральне число)", color="black")
        a = ft.TextField(label="Введіть a", color="black")
        b = ft.TextField(label="Введіть b", color="black")
        result = ft.Text(color="black")

        def calculate(e):
            try:
                n_val, a_val, b_val = int(n.value), float(a.value), float(b.value)

                write_file("cyclic.txt", {"n": n_val, "a": a_val, "b": b_val})

                res = 1.0
                b_i = 1
                a_i = 1

                if radio_group.value == "0":
                    while a_i <= n_val:
                        while b_i <= n_val:
                            res *= (a_val**4 + b_i**4) / (a_val**4 - b_i**4)
                            b_i += 1

                        res *= (a_i**4 + b_val**4) / (a_i**4 - b_val**4)
                        a_i += 0.25

                elif radio_group.value == "1":
                    while a_i <= n_val:
                        a_i += 0.25
                        while b_i <= n_val:
                            res *= (a_i**4 + b_i**4) / (a_i**4 - b_i**4)
                            b_i += 1

                result.value = f"Результат: {res:.4f}"
            except Exception as err:
                result.value = f"Помилка: {err}--> Неправельно введені дані, переконайтеся, що не відбувається ділення на нуль чи під кореневий вираз менше за '0' або інше"
            page.update()

        def load_from_file_cyclic_alg(e):
            data = read_file("cyclic.txt", cyclic_dic)
            n.value = str(data["n"])
            a.value = str(float(data["a"]))
            b.value = str(float(data["b"]))
            calculate(e)
            page.update()

        page.add(
            ft.Column(
                [
                    n,
                    a,
                    b,
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "Обчислити",
                                on_click=calculate,
                                bgcolor="#FFDAC1",
                                color="black",
                            ),
                            ft.ElevatedButton(
                                "Відобразити алгоритм",
                                on_click=show_alg,
                                bgcolor="#FFDAC1",
                                color="black",
                            ),
                        ]
                    ),
                    ft.ElevatedButton(
                        "Зчитати з файлу",
                        on_click=load_from_file_cyclic_alg,
                        bgcolor="#FF9AA2",
                        color="black",
                    ),
                    ft.ElevatedButton(
                        "Головне меню",
                        on_click=show_main,
                        bgcolor="#FF9AA2",
                        color="black",
                    ),
                    result,
                ]
            )
        )
        page.update()

    show_main(None)


ft.app(target=main)
