from tkinter import *

# Crear la ventana principal
ventana = Tk()
ventana.title("Ejemplo de Frame")

# Configurar la ventana principal
ventana.geometry("400x300+500+400")
ventana.config(bg="grey")

# Crear el frame
frame = Frame(ventana)

# Configurar el frame
frame.config(bg="blue" )



# Empaquetar el frame dentro de ventana
frame.pack(fill="x", expand=1)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()