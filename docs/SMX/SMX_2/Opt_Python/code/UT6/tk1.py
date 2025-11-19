import tkinter as tk
from tkinter import Tk

# Crear la ventana principal
ventana = Tk()
ventana.title("Ejemplo de Frame")

# Crear un frame dentro de la ventana principal
frame = tk.Frame(ventana, width=300, height=200, bg="lightblue")
frame.pack()


# Iniciar el bucle principal de Tkinter
ventana.mainloop()