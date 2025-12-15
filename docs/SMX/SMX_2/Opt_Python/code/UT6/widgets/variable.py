from tkinter import *

ventana = Tk()
ventana.title("Ejemplo de variables")
ventana.geometry("300x150+250+300")

nombre = StringVar(ventana)
mostrar = IntVar(ventana)

nombre.set("Mi primera variable")
mostrar.set(1234)

introducir_texto = Entry(ventana, textvariable=nombre, width=25)
etiqueta = Label(ventana, textvariable=mostrar)

introducir_texto.pack(padx=20, pady=20)
etiqueta.pack(padx=10, pady=5)

ventana.mainloop()
