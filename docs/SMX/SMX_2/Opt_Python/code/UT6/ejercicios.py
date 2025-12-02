# ejercicio 1 

# import tkinter as tk
from tkinter import *
ventana=Tk()

# ventana = tk.Tk()
# ventana.title("Práctica 1")
# ventana.geometry("800x450")
# ventana.resizable(False, False)
# ventana.iconbitmap("python.ico")
# ventana.attributes("-alpha", 0.9)

# ventana.mainloop()



















# ejercicio 2
# import tkinter as tk

# ventana = tk.Tk()
# ventana.title("Práctica 2")

# # Resolución de la ventana
# ancho = 960
# alto = 540

# Calcular posición centrada
# pantalla_ancho = ventana.winfo_screenwidth()
# pantalla_alto = ventana.winfo_screenheight()
# x = (pantalla_ancho // 2) - (ancho // 2)
# y = (pantalla_alto // 2) - (alto // 2)

# ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
# ventana.minsize(640, 360)
# ventana.maxsize(1280, 720)

# ventana.mainloop()

# ejercicio 3
import tkinter as tk

ventana = tk.Tk()
ventana.title("Práctica 3")
# ventana.attributes("-fullscreen", False)
ventana.attributes("-fullscreen", True)
ventana.attributes("-toolwindow", True)
# ventana.attributes("-topmost", True)
ventana.configure(bg="blue")                # Fondo azul
# ventana.attributes("-transparentcolor", "blue")   # El color azul se vuelve transparente
ventana.configure(cursor="hand2") 
ventana.mainloop()
