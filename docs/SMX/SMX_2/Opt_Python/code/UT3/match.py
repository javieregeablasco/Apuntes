print("Comienzo programa")

while True: 
  opcion = input("Elige una opción (1, 2 o 3): ")
  if opcion == "no":
     break
  
  match opcion:
    case "1":
        print("Has elegido la opción 1.")
    case "2":
        print("Has elegido la opción 2.")
    case "3":
        print("Has elegido la opción 3.")
    case _:
        print("Opción no válida.")

print("Programa finalizado")