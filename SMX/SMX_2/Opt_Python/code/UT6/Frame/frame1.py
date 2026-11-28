# from tkinter import *
# # Crear la ventana principal
# ventana = Tk()
# ventana.title("Ejemplo de Frame")

# ventana.attributes("-alpha", 0.8)         # Ventana semitransparente
# # ventana.attributes("-fullscreen", True)   # Modo pantalla completa
# ventana.attributes("-transparentcolor", "blue")   # Si el bg de la venta es azul, pasará a transparente
# # Crear un frame dentro de la ventana principal
# # frame = Frame(ventana)
# # frame.config(width=480, height=320, bg="lightblue")
# # frame.pack()

# # Iniciar el bucle principal de Tkinter
# ventana.mainloop()

from tkinter import *
root = Tk()
root.title("Ejemplo 3")
root.geometry("400x400+500+200")

# Frame NW 
marco_4 = Frame(root, bg="yellow", width=400, height=100)
marco_4.pack(anchor=NW)

# Frame SE
marco_1 = Frame(root, bg="red", width=400, height=100)
marco_1.pack(anchor=SE, expand=True)

# Frame SW
marco_2 = Frame(root, bg="blue", width=400, height=100)
marco_2.pack(anchor=SW, expand=True)

# Frame SE
marco_3 = Frame(root, bg="green", width=400, height=100)
marco_3.pack(anchor=SE, expand=True)

root.mainloop()