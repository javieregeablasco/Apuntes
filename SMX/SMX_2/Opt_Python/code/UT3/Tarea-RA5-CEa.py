lista_1 = [1,2,3,4,5,6,7,8,9]
lista_2 = ["azul","verde","amarillo","naranja","cian","magenta","ambar","negro","blanco"]

for indice, color in zip(lista_1,lista_2):
  print("Indice \t y \tcolor: \n", indice, "\t\t", color," ", sep=">>>")

