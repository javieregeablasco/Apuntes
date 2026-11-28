# from tkinter import *
# root = Tk()
# root.title("Ejemplo de grid")
# root.geometry("600x400+500+200")

# ventana1 = Frame(root, bg="yellow", height=200, width=300)
# ventana1.grid(row=0, column=0, columnspan=3, sticky=NSEW)

# ventana2 = Frame(root, bg="red", height=200, width=200)
# ventana2.grid(row=0, column=3, columnspan=2, sticky=NSEW)

# ventana3 = Frame(root, bg="blue", height=200, width=600)
# ventana3.grid(row=1, column=0, columnspan=6, sticky=NSEW)

# root.mainloop()


from tkinter import *
root = Tk()
root.title("Ejemplo de grid")
root.geometry("600x400+500+200")
ventana1 = Frame(root, bg="yellow", height=100, width=100)
ventana1.grid(row=0, column=0, columnspan=3, sticky=W)

ventana2 = Frame(root, bg="red", height=100, width=100)
ventana2.grid(row=0, column=3, columnspan=2, sticky=E)

ventana3 = Frame(root, bg="cyan", height=200, width=100)
ventana3.grid(row=0, column=5, columnspan=1, sticky=NSEW)

ventana4 = Frame(root, bg="blue", height=200, width=600)
ventana4.grid(row=1, column=0, columnspan=6, sticky=NSEW)

root.mainloop()
