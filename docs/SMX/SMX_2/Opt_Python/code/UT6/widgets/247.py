# from tkinter import *

# root = Tk()
# root.title("Ejercicio 1")

# label = Label(root, text="¡Mi primera etiqueta!", state="normal")
# label.pack(anchor=CENTER)

# label.config(
#     fg="blue",       
#     bg="green",      
#     font=("Verdana", 24)
# )
# root.mainloop()

#####################################

# import tkinter as tk
# from tkinter import *

# root = tk.Tk()
# root.title("Ejercicio 2")

# # Etiqueta superior (izquierda)
# label_sup = Label(root, text="Etiqueta superior (izquierda)")
# label_sup.pack(side=TOP, anchor=W, padx=10, pady=5)

# # Etiqueta central
# label_centro = Label(root, text="¡Mi primera etiqueta!")
# label_centro.pack(side=TOP, anchor=CENTER, pady=10)
# label_centro.config(
#     fg="blue",
#     bg="green",
#     font=("Verdana", 24)
# )

# # Etiqueta inferior (derecha)
# label_inf = Label(root, text="Etiqueta inferior (derecha)")
# label_inf.pack(side=TOP, anchor=E, padx=10, pady=5)

# root.mainloop()

#########################################3

from tkinter import *

root = Tk()
root.title("Ejercicio 3")
root.geometry("250x100+300+300")

label = Label(root, text="Nombre")
label.grid(row=0, column=0, sticky=W, padx=5, pady=15)

entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)

label2 = Label(root, text="Apellidos")
label2.grid(row=1, column=0, sticky=W, padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()

