import tkinter as tk

root = tk.Tk()
root.title("Diferencia entre highlightbackground y highlightcolor")

# Crear un Entry para poder mover el foco entre widgets
entry = tk.Entry(root)
entry.pack(pady=10)

frame = tk.Frame(
    root,
    width=250,
    height=120,
    highlightthickness=4,       # Grosor de la línea de resaltado
    highlightbackground="red",  # Color del borde cuando NO tiene foco
    highlightcolor="green"      # Color del borde cuando SÍ tiene foco
)
frame.pack(pady=10)

# Pulsar sobre el frame para darle foco
frame.bind("<Button-1>", lambda e: frame.focus_set())

root.mainloop()
