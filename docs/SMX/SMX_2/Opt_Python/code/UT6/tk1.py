# import tkinter as tk
# from tkinter import Tk

# # Crear la ventana principal
# ventana = Tk()
# ventana.title("Ejemplo de Frame")

# # Crear un frame dentro de la ventana principal
# frame = tk.Frame(ventana, width=300, height=200, bg="lightblue")
# frame.pack()

# # Iniciar el bucle principal de Tkinter
# ventana.mainloop()


from logging import root
import tkinter as tk
from tkinter import Tk
# Crear la ventana principal
ventana = Tk() 
ventana.title("Mi primera ventana")
ventana.geometry("400x300+100+100")
ventana.resizable(True, False)
ventana.configure(bg="blue")
ventana.iconbitmap("favicon.ico")

# Iniciar el bucle principal de Tkinter
ventana.mainloop()