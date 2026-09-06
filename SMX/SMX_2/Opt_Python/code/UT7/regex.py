# print("primera linea\t fragmento de texto \n")
# print("segunda linea\f")
# print("tercera linea")

# import re
# # Ejemplo de uso de search()
# patron = r'[0-9]{3}-[0-9]{2}-[0-9]{4}'  # Patrón para un número de seguro social
# # patron = r'\d{3}-\d{2}-\d{4}'  # Mismo patrón con secuencias especiales
# texto = "Mi número de seguro social es 123-45-6789."
# coincidencia = re.search(patron, texto)  # Busca la primera coincidencia
# if coincidencia:
#     print("Coincidencia encontrada:", coincidencia.group())  # group() recupera el texto que ha coincidido
# else:
#     print("No se encontró ninguna coincidencia.")


# import re
# # Ejemplo de uso de match() y fullmatch()
# patron = r'\d{3}-\d{2}-\d{4}'  # Patrón
# texto1 = "123-45-6789 es mi número de seguro social."
# texto2 = "Mi número de seguro social es 123-45-6789."
# coincidencia_match = re.match(patron, texto1)  # Busca coincidencia al comienzo
# coincidencia_fullmatch = re.fullmatch(patron, texto2)  # Busca coincidencia en toda la cadena
# if coincidencia_match:
#     print("Coincidencia match encontrada:", coincidencia_match.group())
# else:
#     print("No se encontró ninguna coincidencia con match.")
# if coincidencia_fullmatch:
#     print("Coincidencia fullmatch encontrada:", coincidencia_fullmatch.group())
# else:
#     print("No se encontró ninguna coincidencia con fullmatch.")  

# import re
# # Ejemplo de uso de findall() y finditer()
# patron = r'\d{3}-\d{2}-\d{4}'  # Patrón

# texto = "Mis números de seguro social son 123-45-6789 y 987-65-4321."

# coincidencias_findall = re.findall(patron, texto)  # Devuelve una lista de todas las coincidencias
# coincidencias_finditer = re.finditer(patron, texto)  # Devuelve un iterador de objetos de coincidencia

# # Visualizar la lista de coincidencias
# print("Coincidencias con findall:", coincidencias_findall)

# # Iterar sobre el iterable obtenido con finditer()
# iteraciones =["Primera iteración: ","Segunda iteración: "]
# iterador=0

# for coincidencia in coincidencias_finditer:
#     print(iteraciones[iterador], coincidencia.group())
#     iterador += 1

import re
# Ejemplo de uso de compile()
patron = r'\d{3}-\d{2}-\d{4}'  # Patrón

regex = re.compile(patron)  # Compila el patrón en un objeto regex 

texto = "Mis números de seguro social son 123-45-6789 y 987-65-4321."

coincidencias = regex.findall(texto)  # Usa el objeto regex para buscar coincidencias
# print(isinstance(coincidencias, list))
print("Coincidencias encontradas:", coincidencias)  # Salida: ['123-45-6789', '987-65-4321']

print("Cantidad de elementos encontrados en la lista:", coincidencias.__len__())

# import re
# # Ejemplo de uso de group()
# patron = r'(\d{3})-(\d{2})-(\d{4})'  # Patrón con grupos
# texto = "Mi número de seguro social es 123-45-6789."
# coincidencia = re.search(patron, texto)  # Busca la primera coincidencia

# print(f"cantidad de coincidencias encontradas: {coincidencia.re.groups}")

# if coincidencia:
#     print("Número completo:", coincidencia.group(0))  # Grupo 0 es el texto completo que coincide
#     # print("Número completo:", coincidencia.group())  # 0 es el valor por defecto de group()
#     print("Coincidencia 1 (111):", coincidencia.group(1))    # Primer grupo
#     print("Coincidencia 2 (11):", coincidencia.group(2))     # Segundo grupo
#     print("Coincidencia 2 (1111):", coincidencia.group(3))   # Tercer grupo
# else:
#     print("No se encontró ninguna coincidencia.")

# import re
# patron = r'\d{3}-\d{2}-\d{4}'  # Patrón
# texto = "Mi número de seguro social es 123-45-6789."
# texto_modificado = re.sub(patron, "ABC-DE-FGHI", texto)  # Reemplaza las coincidencias con "ABC-DE-FGHI"
# print("Texto modificado:", texto_modificado)   