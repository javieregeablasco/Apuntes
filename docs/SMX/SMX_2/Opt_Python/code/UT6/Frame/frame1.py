from tkinter import *
# Crear la ventana principal
ventana = Tk()
ventana.title("Ejemplo de Frame")

ventana.attributes("-alpha", 0.8)         # Ventana semitransparente
# ventana.attributes("-fullscreen", True)   # Modo pantalla completa
ventana.attributes("-transparentcolor", "blue")   # Si el bg de la venta es azul, pasará a transparente
# Crear un frame dentro de la ventana principal
# frame = Frame(ventana)
# frame.config(width=480, height=320, bg="lightblue")
# frame.pack()

# Iniciar el bucle principal de Tkinter
ventana.mainloop()