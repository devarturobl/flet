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


# Personalizando proyecto

Este bloque usa el decorador @ft.control para crear plantillas de botones heredando de ft.Button:
CalcButton: Establece que todos los botones se expandan de forma equitativa (expand=1).

DigitButton, ActionButton y ExtraActionButton: Heredan de la anterior, pero aplican combinaciones específicas de colores de fondo (bgcolor) y de texto (color) según su función.

Estructura y Diseño Visual (page.add)
Aquí se define cómo se organiza visualmente la calculadora utilizando contenedores:

ft.Container: Envuelve la calculadora para darle un ancho de 350 píxeles, fondo negro, bordes redondeados y un margen interno (padding).

ft.Column: Organiza los elementos de arriba hacia abajo (verticalmente).

ft.Row: Organiza los elementos de izquierda a derecha (horizontalmente). La primera fila muestra el texto result alineado a la derecha, y las siguientes filas contienen los botones personalizados organizados en cuadrícula.

4. 🚀 Ejecución
La última línea, ft.app(target=main), le dice a Flet que inicie la aplicación ejecutando todo lo que programamos dentro de la función main.

¿Qué parte de esta estructura te gustaría que analicemos en detalle primero? Elige una opción:

El diseño con Columnas y Filas (ft.Column y ft.Row): Cómo se organizan los botones en la pantalla de la calculadora.

Los botones personalizados: Cómo funcionan las clases como DigitButton y por qué nos ahorran escribir mucho código repetido.

La propiedad expand: Por qué el botón "0" tiene expand=2 a diferencia de los demás botones.
