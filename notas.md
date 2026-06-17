# Creamos un nuevo proyecto y un entorno virtual
pyhon -m venv nombre
Despues en command palette selecionamos Python interpreter

# Instalacion
pip install flet[all]

# Codigo basico

import flet as ft

def main(page: ft.Page):
    texto = ft.Text("HOlá, mundo!")
    page.add(texto)

ft.app(target=main)

en flet se crea la funcion main en donde se incorpora la libreria ft
despues se crea un objeto el cual se iguala al componente de ft en este caso Text
por ultimo se incorpora mediante el objeto principal que es page con add y el elemento que creamos

por ultimo con ft.app mandamos el target que es la funcion principal main

# Previsualizar en web

flet run --web main.py 

