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
 
from tkinter import  *
import sys

sys.path.append("C:\\Users\\titan\\Documents\\GitHub\\githubpages\\Apuntes\\docs\\SMX\\SMX_2\\Opt_Python\\code\\UT6")
#from tkinter import Tk, Toplevel

# Crear la ventana principal
ventana = Tk() 
ventana.configure(bg="blue")
ventana.geometry("800x450")
ventana.wm_iconbitmap("favicon.ico")
# ventana.attributes('-topmost', True)
# print(type(ventana.configure()))

ventana.config(bg="lightgray")        # Cambia el color de fondo de la ventana
ventana.config(cursor="hand2")        # Cambia el cursor al estilo de "mano"
ventana.configure(relief="ridge", bd=25)  # Aplica un borde en relieve



ventana.mainloop()

# ventana.title("Mi primera ventana")
# ventana.wm_maxsize(500,500)
# ventana.state("zoomed")
# ventana.geometry("1000x250+100+250")
# ventana.configure(cursor="mouse") 
# ventana.geometry("400x300+100+100")
# ventana.resizable(True, True)
# ventana.configure(bg="blue")
# frame = tk.Frame(ventana, width=300, height=200, bg="lightblue")

# frame.pack()
# ventana.iconbitmap("favicon.ico")

# Iniciar el bucle principal de Tkinter
 
# ventana1 = Toplevel(ventana)
# ventana1.title("Mi segunda ventana")
# ventana1.geometry("400x300+400+400")
# ventana1.resizable(True, True)
# # ventana.configure(bg="blue")
# frame1 = tk.Frame(ventana1, width=300, height=200, bg="salmon")

# frame.pack(pady=20)
# ventana.iconbitmap("favicon.ico")

# Iniciar el bucle principal de Tkinter

