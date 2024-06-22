# app.py
import flet as ft

def main(page: ft.Page):
    # Función que maneja el evento del botón
    def button_clicked(e):
        print("Botón presionado!")

    # Crear un botón
    button = ft.ElevatedButton(text="Presioname", on_click=button_clicked)
    
    # Agregar el botón a la página
    page.add(button)

# Iniciar la aplicación
ft.app(target=main)
