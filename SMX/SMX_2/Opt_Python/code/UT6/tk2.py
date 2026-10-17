import tkinter as tk

# Función que se ejecuta al hacer clic en el botón
def boton_clic():
    print("¡Botón clickeado!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Manejo de Eventos")
ventana.geometry("300x200+500+500")
ventana.configure(bg="blue")
ventana.resizable(True, True)

# Crear un frame dentro de la ventana principal
frame = tk.Frame(ventana, width=200, height=150, bg="lightblue")
frame.pack()
frame.pack_propagate(False)

# Crear un botón y asignar el controlador de eventos
boton = tk.Button(frame, text="Clic aquí", command=boton_clic)
boton.pack(expand=True)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()

 