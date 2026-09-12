from tkinter import *

def mostrar_opcion():
    print("Opción seleccionada:", opcion.get())


root = Tk()
root.config(bg="black")
root.config(width=400, height=100)
root.geometry("400x100+400+400")

opcion = StringVar(value="1")

rb1 = Radiobutton(root, text="Opción 1", variable=opcion, value="1", command=mostrar_opcion)
rb2 = Radiobutton(root, text="Opción 2", variable=opcion, value="2", command=mostrar_opcion)

rb1.pack(side="top")
rb2.pack(side="top")

root.mainloop()





