# ejercicio 1 

# import tkinter as tk
# from tkinter import *
# ventana=Tk()

# ventana.title("Mi primera ventana")
# ventana.geometry("800x450+200+100")
# ventana.resizable(True, False)
# ventana.config(bg="blue", cursor="heart")

# # ventana.iconbitmap("python.ico")
# ventana.attributes("-alpha", 0.9)

# ventana.mainloop()


# ejercicio 2

# from tkinter import *

# ventana = Tk()
# ventana.title("Ejercicio 2")

# # Resolución de la ventana
# ancho = 600
# alto = 400

# # Calcular posición centrada
# pantalla_ancho = ventana.winfo_screenwidth()
# pantalla_alto = ventana.winfo_screenheight()

# x = (pantalla_ancho // 2) - (ancho // 2)
# y = (pantalla_alto // 2) - (alto // 2)

# ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
# ventana.attributes(transparentcolor="yellow", alpha=0.85)
# ventana.minsize(640, 360)
# ventana.maxsize(1280, 720)

# ventana.mainloop()

# ejercicio 3
from tkinter import *

ventana = Tk()
ventana.title("Ejercicio 3")
ventana.attributes("-fullscreen", True)
ventana.attributes("-toolwindow", False)
ventana.configure(bg="blue")                
ventana.resizable(False,False)
ventana.configure(cursor="hand2") 

ventana.mainloop()
