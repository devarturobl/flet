import flet as ft


def main(page: ft.Page):
    page.title = "Calculadora Ejemplo"
    result = ft.Text(value="0", size=30)

    expression = ""

    def on_click(e):
        nonlocal expression
        v = e.control.data
        if v == "C":
            expression = ""
            result.value = "0"
        elif v == "=":
            try:
                expression = str(eval(expression))
                result.value = expression
            except Exception:
                result.value = "Error"
                expression = ""
        else:
            expression += v
            result.value = expression
        page.update()

    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
    ]

    rows = [ft.Row(controls=[result], alignment=ft.MainAxisAlignment.END)]

    for row in buttons:
        controls = []
        for b in row:
            controls.append(ft.ElevatedButton(b, data=b, on_click=on_click, width=60))
        rows.append(ft.Row(controls=controls))

    rows.insert(1, ft.Row(controls=[ft.ElevatedButton("C", data="C", on_click=on_click)]))

    page.add(ft.Column(controls=rows))


if __name__ == "__main__":
    ft.app(target=main)
