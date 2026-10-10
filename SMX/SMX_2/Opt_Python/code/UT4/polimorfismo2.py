from abc import ABC, abstractmethod

class Animales(ABC):
  def __init__(self, raza, familia, carnivoro, herbivoro, patas):
    self.raza = raza
    self.familia = familia
    self.carnivoro = carnivoro
    self.herbivoro = herbivoro
    self.patas = patas

  def se_alimenta(self):
    match(self.carnivoro, self.herbivoro):
      case (True, False):
        return f"El {self.raza} es un animal carnívoro."
      case (False, True):
        return f"El {self.raza} es un animal herbívoro."
      case (True, True):
        return f"El {self.raza} es un animal omnívoro."
      case _:
        return f"El {self.raza} no tiene un tipo de alimentación definido." 
      
  def se_desplaza(self):
    if self.patas == 2: 
      return f"El animal {self.raza} de la familia {self.familia} es un bipedo."
    elif self.patas == 4:
      return f"El animal {self.raza} de la familia {self.familia} es un cuadrupedo."
    else:
      return f"El animal {self.raza} de la familia {self.familia} tiene una forma de desplazamiento especial."
    
  def vocalizacion(self, sonido):
    return f"El {self.raza} emite el sonido: {sonido}"  
  
  @abstractmethod
  def comunicarse(self):
    """Método abstracto que obliga a las clases hijas a implementar su propia vocalización."""
    pass
  
class Perro(Animales):
  def comunicarse(self):
    return f"El {self.raza} ladra: ¡Guau guau!"

class Gato(Animales):
  def comunicarse(self):
    return f"El {self.raza} maúlla: ¡Miau!"

class Pajaro(Animales):
  def comunicarse(self):
    return f"El {self.raza} canta: ¡Pío pío!"

perro = Perro("Pastor Alemán", "Caninos", True, False, 4)
gato = Gato("Siames", "Felinos", True, False, 4)
pajaro = Pajaro("Canario", "Aves", False, True, 2)

animales = [perro, gato, pajaro]

for animal in animales:
  print(animal.se_alimenta())
  print(animal.se_desplaza())
  print(animal.comunicarse())  # Método que Python exige definir en cada subclase
  print("----")

