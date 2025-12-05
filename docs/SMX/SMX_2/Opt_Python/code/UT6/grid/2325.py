'''ejercicio 1'''
# import tkinter as tk

# ventana = tk.Tk()
# ventana.title("Ejercicio 1")

# # Tamaño libre (ejemplo)
# ventana.geometry("400x150")

# # Crear frames con colores y tamaños (libre elección)
# frame1 = tk.Frame(ventana, bg="red",   width=100, height=100)
# frame2 = tk.Frame(ventana, bg="green", width=100, height=100)
# frame3 = tk.Frame(ventana, bg="blue",  width=100, height=100)

# # Colocación de los frames según el enunciado
# frame1.grid(row=0, column=0)
# frame2.grid(row=0, column=1)
# frame3.grid(row=0, column=3)   # salto a la columna 3

# # Lanzar eventos
# ventana.mainloop()


'''ejercicio 2'''
# import tkinter as tk

# ventana = tk.Tk()
# ventana.title("Ejercicio 2")

# # Tamaño libre (ejemplo)
# ventana.geometry("300x300")

# # Crear frames
# frame1 = tk.Frame(ventana, bg="red",    width=150, height=150)
# frame2 = tk.Frame(ventana, bg="green",  width=150, height=150)
# frame3 = tk.Frame(ventana, bg="blue",   width=150, height=150)
# frame4 = tk.Frame(ventana, bg="violet", width=150, height=150)

# # Colocar frames según el enunciado
# frame1.grid(row=0, column=0)
# frame2.grid(row=0, column=1)
# frame3.grid(row=1, column=0)
# frame4.grid(row=1, column=1)

# # Lanzar eventos
# ventana.mainloop()


'''ejercicio 3'''
# import tkinter as tk

# ventana = tk.Tk()
# ventana.title("Ejercicio 3")

# # Tamaño libre (ejemplo)
# ventana.geometry("300x300")

# # Crear frames
# frame1 = tk.Frame(ventana, bg="red",    width=150, height=150)
# frame2 = tk.Frame(ventana, bg="green",  width=150, height=150)
# frame3 = tk.Frame(ventana, bg="blue",   width=150, height=150)
# frame4 = tk.Frame(ventana, bg="violet", width=50, height=50)

# # Colocar frames según el enunciado
# frame1.grid(row=0, column=0)
# frame2.grid(row=0, column=1)
# frame3.grid(row=1, column=0)
# frame4.grid(row=1, column=1, sticky="N")

# # Lanzar eventos
# ventana.mainloop()

'''ejercicio 4'''
# import tkinter as tk

# ventana = tk.Tk()
# ventana.title("Ejercicio 4")

# # Tamaño libre
# ventana.geometry("400x300")

# # Crear frames (colores para identificar)
# frame1 = tk.Frame(ventana, bg="lightgray", width=380, height=80,)   # HEADER
# frame2 = tk.Frame(ventana, bg="lightblue", width=150, height=200)  # SIDEBAR
# frame3 = tk.Frame(ventana, bg="lightgreen", width=230, height=200) # CONTENT

# # HEADER ocupa 2 columnas → usar columnspan
# frame1.grid(row=0, column=0, columnspan=2)

# # Segunda fila: sidebar y content
# frame2.grid(row=1, column=0)
# frame3.grid(row=1, column=1)

# # Lanzar eventos
# ventana.mainloop()

'''ejercicio 5'''
import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejercicio 5")

# Tamaño libre
ventana.geometry("400x300")

# Crear frames (colores para identificar)
frame1 = tk.Frame(ventana, bg="lightgray", width=380, height=80,)   # HEADER
frame2 = tk.Frame(ventana, bg="lightblue", width=150, height=200)  # SIDEBAR
frame3 = tk.Frame(ventana, bg="lightgreen", width=230, height=200) # CONTENT

# HEADER ocupa 2 columnas → usar columnspan
frame1.grid(row=0, column=0, columnspan=2, sticky="NSEW")

# Segunda fila: sidebar y content
frame2.grid(row=1, column=0, sticky="NSEW")
frame3.grid(row=1, column=1, sticky="NSEW")

# Hacer que las filas y columnas crezcan
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)  

ventana.grid_rowconfigure(0, weight=1)      
ventana.grid_rowconfigure(1, weight=4)      

# Lanzar eventos
ventana.mainloop()
