from tkinter import filedialog as FileDialog

# fichero = FileDialog.askopenfilename(title="Abrir un fichero")
fichero = FileDialog.asksaveasfilename(title="Guardar fichero")
print("La ruta del fichero es:", fichero)
