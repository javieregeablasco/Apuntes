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
 
import tkinter as tk
from tkinter import Tk, Toplevel

# Crear la ventana principal
ventana = Tk() 
ventana.title("Mi primera ventana")
# ventana.geometry("400x300+100+100")
ventana.resizable(True, True)
# ventana.configure(bg="blue")
frame = tk.Frame(ventana, width=300, height=200, bg="lightblue")

frame.pack()
# ventana.iconbitmap("favicon.ico")

# Iniciar el bucle principal de Tkinter
 
ventana1 = Toplevel(ventana)
ventana1.title("Mi segunda ventana")
ventana1.geometry("400x300+400+400")
ventana1.resizable(True, True)
# ventana.configure(bg="blue")
frame1 = tk.Frame(ventana1, width=300, height=200, bg="salmon")

frame.pack(pady=20)
# ventana.iconbitmap("favicon.ico")

# Iniciar el bucle principal de Tkinter
ventana1.mainloop()

