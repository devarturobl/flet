import flet as ft

def main(page: ft.Page):
    my_texto = ft.Text("HOlá, mundo!")
    page.add(my_texto)

ft.app(target=main)
