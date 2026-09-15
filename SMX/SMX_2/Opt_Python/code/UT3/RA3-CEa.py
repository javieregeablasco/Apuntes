# Programa para comprobar qué años son bisiestos desde 0 hasta un valor dado
while True:
# Pedir un valor entero
  anyo = int(input("Introduce un año límite: "))

  #print("Años bisiestos desde 0 hasta", limite, ":")

  # Recorrer todos los años desde 0 hasta el valor introducido
  #for año in range(limite + 1):
  print ("condicion 1", anyo % 4 == 0)
  print("condicion2:", anyo % 100 != 0)
  print("condicion3", anyo % 400 == 0)
          
  print("bisiesto¿?: ", (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 4 == 0 and anyo % 100 == 0) and anyo % 400 == 0)        