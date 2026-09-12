# from tkinter import *
# root = Tk()
 
# label = Label(root,text="¡Hola Mundo!")
# label.pack()

# root.mainloop() 


# import os
# print("directorio:", os.getcwd())

from tkinter import *

directory= "C://Users//titan//Documents//GitHub//githubpages//Apuntes//docs//SMX//SMX_2//Opt_Python//code//UT6//widgets//"

root = Tk()
root.iconbitmap(directory+"favicon.ico")
root.title("Etiqueta Label")

imagen = PhotoImage(file=directory+"imagen.png")

label = Label(
     root,
     text="Texto de ejemplo",
     font=("Arial", 24, "bold italic"),
     fg="white",
     bg="#333333",
     padx=20,
     pady=10,
     compound="bottom",
     image=imagen
)

label.pack()

root.mainloop()