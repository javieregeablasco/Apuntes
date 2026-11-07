from tkinter import *

root = Tk()
root.title("Demostración de fill y expand")
root.geometry("500x350")

# --- Marco para los botones de control ---
control = Frame(root, pady=10)
control.pack(fill="x")

# Variables de selección
fill_var = StringVar(value="none")
expand_var = BooleanVar(value=False)

# Selector de fill
Label(control, text="fill:").grid(row=0, column=0)
OptionMenu(control, fill_var, "none", "x", "y", "both").grid(row=0, column=1, padx=10)

# Selector de expand
Label(control, text="expand:").grid(row=0, column=2)
Checkbutton(control, text="True / False", variable=expand_var).grid(row=0, column=3, padx=10)

# --- Zona de prueba ---
zona = Frame(root, bg="#dddddd", width=450, height=250)
zona.pack(pady=10, fill="both", expand=True)

# Widget de prueba
test = Label(zona, text="Widget de prueba", bg="skyblue")

# Función para aplicar pack con nuevos parámetros
def actualizar():
    test.pack_forget()  # Limpia el pack anterior
    fill = fill_var.get()
    if fill == "none":
        test.pack(expand=expand_var.get())
    else:
        test.pack(fill=fill, expand=expand_var.get())

# Botón para aplicar los cambios
Button(control, text="Aplicar", command=actualizar).grid(row=0, column=4, padx=20)

root.mainloop()
