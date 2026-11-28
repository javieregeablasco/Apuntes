from tkinter import * 

# Función evento de radiobutton
def mostrar_seleccion():
    opcion = seleccion.get()
    print(f"Opción seleccionada: {opcion}")
    
# Función recuperar valor de radiobutton
# y escribir valor en variable de control `mostrar``
def cambio(*args):
    mostrar.set(seleccion.get())

# Ventana root
root = Tk()
root.title("Ejercicio 1")
root.geometry("250x150+300+200")

# Variables de control
seleccion = IntVar(root)
mostrar = StringVar(root)

# Radiobuttons
rb_1 = Radiobutton(root, text="Opción 1", variable=seleccion, value=1, command=mostrar_seleccion)
rb_2 = Radiobutton(root, text="Opción 2", variable=seleccion, value=2, command=mostrar_seleccion)
rb_3 = Radiobutton(root, text="Opción 3", variable=seleccion, value=3, command=mostrar_seleccion)
rb_4 = Radiobutton(root, text="Opción 4", variable=seleccion, value=4, command=mostrar_seleccion)

# Etiqueta que pinta el valor de radiobutton seleccionado
texto = Label(root, text="Opción seleccionada:",justify="right")
etiqueta = Label(root,textvariable=mostrar)

# Llamar a funcion `cambio` cada vez que se detecta un cambio 
# en variable de control `seleccion`
seleccion.trace("w",cambio)

# Grid de 2x2 para radiobutton
rb_1.grid(row=0, column=0, padx=20, pady=10)
rb_2.grid(row=0, column=1, padx=20, pady=10)
rb_3.grid(row=1, column=0, padx=20, pady=10)
rb_4.grid(row=1, column=1, padx=20, pady=10)

# Pintar labels debajo de radiobuttons
etiqueta.grid(row=3, column=1)
texto.grid(row=3, column=0, pady=10)

root.mainloop()