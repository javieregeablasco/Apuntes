from tkinter import *

contador = 0

root = Tk()
root.title("Boton")
root.geometry("300x60+500+400")


def saludar(*args):
    global contador 
    contador += 1
    print(f"El botón ha sido pulsado {contador} veces")

boton = Button(root, text="Aceptar", command=lambda:saludar())

boton.pack(pady=10)

root.mainloop()