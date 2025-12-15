from tkinter import *

def mostrar_estado():
    print("Estado del checkbutton:", activar.get())

root = Tk()
root.config(bg="black")
root.config(width=400, height=100)
root.geometry("400x100+400+400")

activar = BooleanVar(value=False)

chk = Checkbutton(root, text="Activar opción",
                     variable=activar,
                     command=mostrar_estado,
                     #indicatoron=OFF)
                 )

chk.pack(side="top", pady=20)

root.mainloop()