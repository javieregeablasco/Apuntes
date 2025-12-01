from tkinter import *
# Crear la ventana principal
ventana = Tk()
ventana.title("Ejemplo de Frame")

# Configurar la ventana principal
ventana.geometry("400x300+500+500")
ventana.config(bg="blue")          # color de fondo, background
ventana.config(cursor="pirate")    # tipo de cursor (arrow defecto)
ventana.config(relief="sunken")    # relieve del root 
ventana.config(bd=25)              # tamaño del borde en píxeles

# Crear un frame dentro de la ventana principal
frame = Frame(ventana)

# Configurar el frame
frame.config(width=400, height=300)
frame.config(cursor="")         # Tipo de cursor
frame.config(relief="sunken")   # relieve del frame hundido
frame.config(bd=25)             # tamaño del borde en píxeles

# Empaquetar el frame dentro de ventana
frame.pack()

# Iniciar el bucle principal de Tkinter
ventana.mainloop()