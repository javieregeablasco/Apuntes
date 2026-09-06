import re
import tkinter as tk
from tkinter import messagebox

# Lista para almacenar correos válidos
correos = []

# Expresión regular para validar correos electrónicos
patron_email = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'


def validar_email():
    email = entrada.get()

    # Validar formato
    if not re.match(patron_email, email):
        messagebox.showerror("Error", "Dirección de correo inválida.")
        entrada.delete(0, tk.END)
        return

    # Comprobar duplicado
    if email in correos:
        messagebox.showwarning("Duplicado", "La dirección ya existe en la lista.")
        entrada.delete(0, tk.END)
        return

    # Si todo es correcto
    correos.append(email)
    messagebox.showinfo("Correcto", "Correo válido y almacenado correctamente.")
    entrada.delete(0, tk.END)


# ----- Interfaz gráfica -----
ventana = tk.Tk()
ventana.title("Validador de correo electrónico")
ventana.geometry("350x150")

etiqueta = tk.Label(ventana, text="Introduzca una dirección de correo:")
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana, width=40)
entrada.pack()

boton = tk.Button(ventana, text="Validar", command=validar_email)
boton.pack(pady=10)

ventana.mainloop()
