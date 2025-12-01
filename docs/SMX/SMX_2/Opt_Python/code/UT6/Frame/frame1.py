from tkinter import *
# Crear la ventana principal
ventana = Tk()
ventana.title("Ejemplo de Frame")

# Crear un frame dentro de la ventana principal
frame = Frame(ventana)
frame.config(width=480, height=320, bg="lightblue")
frame.pack()

# Iniciar el bucle principal de Tkinter
ventana.mainloop()