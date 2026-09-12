from tkinter import *
root = Tk()
root.title("Ejemplo de anchors")
root.geometry("400x400+500+200")

# Frame NW 
marco_4 = Frame(root, bg="yellow", width=400, height=100)
marco_4.pack(anchor=NW)

# Frame SE
marco_1 = Frame(root, bg="red", width=400, height=100)
marco_1.pack(anchor=SE, expand=True)

# Frame SW
marco_2 = Frame(root, bg="blue", width=400, height=100)
marco_2.pack(anchor=SW, expand=True)

# Frame SE
marco_3 = Frame(root, bg="green", width=400, height=100)
marco_3.pack(anchor=SE, expand=True)

root.mainloop()


# from tkinter import *

# root = Tk()
# root.title("Ejemplo 1")
# root.geometry("300x200+500+400")

# marco_1 = Frame(root, bg="blue", width=300, height=100)
# marco_1.pack(fill="x")

# marco_2 = Frame(root, bg="gray", height=100, width=100)
# marco_2.pack(expand=True, fill="y", anchor=CENTER)

# root.mainloop()


# from tkinter import *

# root = Tk()
# root.title("Ejemplo 2")

# marco1 = Frame(root, bg="red", width=130, height=200)
# marco1.pack(side="left", expand=True, fill="both", padx=5, pady=5)
# marco2 = Frame(root, bg="green", width=130, height=200)
# marco2.pack(side="left", expand=True, fill="both", padx=5, pady=5)
# marco3 = Frame(root, bg="blue", width=130, height=200)
# marco3.pack(side="left", expand=True, fill="both", padx=5, pady=5)

# root.mainloop()

# from tkinter import *

# root = Tk()
# root.title("Ejercicio 3")

# frame1 = Frame(root)
# frame1.pack(side="left", pady=20, padx=10)

# frame2 = Frame(root)
# frame2.pack(side="left", pady=20, padx=10)

# root.mainloop()