'''SET'''
# from tkinter import *

# ventana = Tk()
# ventana.title("Ejemplo de variables")
# ventana.geometry("300x150+250+300")

# nombre = StringVar(ventana)
# mostrar = IntVar(ventana)

# nombre.set("Mi primera variable")
# mostrar.set(1234)

# introducir_texto = Entry(ventana, textvariable=nombre, width=25)
# etiqueta = Label(ventana, textvariable=mostrar)

# introducir_texto.pack(padx=20, pady=20)
# etiqueta.pack(padx=10, pady=5)

# ventana.mainloop()

'''GET'''
# from tkinter import *

# ventana = Tk()
# ventana.title("get y set")
# ventana.geometry("300x150+250+300")

# nombre = StringVar(ventana)
# mostrar = StringVar(ventana)

# def escribir():
#   mostrar.set(nombre.get())
  
# introducir_texto = Entry(ventana, textvariable=nombre, width=25)
# etiqueta = Label(ventana, textvariable=mostrar)
# boton = Button(ventana, text="Aceptar", command=escribir)

# introducir_texto.pack(pady=20)
# etiqueta.pack(pady=5)
# boton.pack(pady=10)

# ventana.mainloop()

'''TRACE'''
from tkinter import *

ventana = Tk()
ventana.title("Método trace")
ventana.geometry("300x100+400+300")

texto = StringVar()
mostrar = StringVar()

def cambio(*args):
    mostrar.set(texto.get())

texto.trace("w", cambio)

entrada = Entry(ventana, textvariable=texto)
etiqueta = Label(ventana, textvariable=mostrar)

entrada.pack(pady=20)
etiqueta.pack(pady=10)

ventana.mainloop()
