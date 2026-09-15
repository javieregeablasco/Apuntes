class Coche():
    cantidad_ruedas = 4
   
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"Coche: {self.marca} {self.modelo}"
    
    def ruedas(self):
        return f"El coche tiene {self.cantidad_ruedas} ruedas."


class Moto():
    cantidad_ruedas = 2
   
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"Moto: {self.marca} {self.modelo}"
    
    def ruedas(self):
        return f"La moto tiene {self.cantidad_ruedas} ruedas."

class Camion():
    cantidad_ruedas = 6

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"Camión: {self.marca} {self.modelo}"
    
    def ruedas(self):
        return f"El camión tiene {self.cantidad_ruedas} ruedas."        
    
def cantidad_ruedas(vehiculo):
    return vehiculo.ruedas()     
    
# Crear objeto
mi_vehiculo = Moto("Honda", "CBR600")
ruedas = cantidad_ruedas(mi_vehiculo)
print(f"La cantidad de ruedas de mi vehiculo es de: {ruedas} ruedas")