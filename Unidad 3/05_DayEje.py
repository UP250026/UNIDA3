# 1. Declarar una lista vacía
empty_list = []

# 2. Declarar una lista con más de 5 elementos
items_list = [1, 2, 3, 4, 5, 6]

# 3. Encontrar la longitud de tu lista
print("Longitud de la lista:", len(items_list))

# 4. Obtener el primer elemento, el del medio y el último elemento de la lista
first_item = items_list[0]
middle_item = items_list[len(items_list) // 2]
last_item = items_list[-1]
print("Primer elemento:", first_item)
print("Elemento del medio:", middle_item)
print("Último elemento:", last_item)

# 5. Declarar una lista llamada mixed_data_types con información personal
mixed_data_types = ["TuNombre", 30, 1.75, "Soltero/a", "TuDirección"]
print("Lista de datos mixtos:", mixed_data_types)

# 6. Declarar una lista de empresas de TI
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Imprimir la lista
print("Empresas de TI:", it_companies)

# 8. Imprimir el número de empresas
print("Número de empresas:", len(it_companies))

# 9. Imprimir la primera, media y última empresa
print("Primera empresa:", it_companies[0])
print("Empresa del medio:", it_companies[len(it_companies) // 2])
print("Última empresa:", it_companies[-1])

# 10. Modificar una empresa y mostrar la lista
it_companies[0] = "Meta"
print("Lista modificada:", it_companies)

# 11. Agregar una empresa de TI
it_companies.append("Spotify")
print("Lista con una empresa añadida:", it_companies)

# 12. Insertar una empresa en el medio
it_companies.insert(len(it_companies) // 2, "Tesla")
print("Lista después de insertar en el medio:", it_companies)

# 13. Cambiar a mayúsculas una empresa (sin incluir IBM)
it_companies[1] = it_companies[1].upper()
print("Lista con una empresa en mayúsculas:", it_companies)

# 14. Unir las empresas con un separador
joined_companies = " #;&nbsp; ".join(it_companies)
print("Empresas unidas:", joined_companies)

# 15. Comprobar si una empresa existe en la lista
company_to_check = "Google"
print(f"¿{company_to_check} está en la lista?", company_to_check in it_companies)

# 16. Ordenar la lista
it_companies.sort()
print("Lista ordenada:", it_companies)

# 17. Revertir el orden de la lista
it_companies.reverse()
print("Lista en orden descendente:", it_companies)

# 18. Extraer las primeras 3 empresas
print("Primeras 3 empresas:", it_companies[:3])

# 19. Extraer las últimas 3 empresas
print("Últimas 3 empresas:", it_companies[-3:])

# 20. Extraer la(s) empresa(s) del medio
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    print("Empresas del medio:", it_companies[middle_index-1:middle_index+1])
else:
    print("Empresa del medio:", it_companies[middle_index])

# 21. Eliminar la primera empresa
it_companies.pop(0)
print("Lista después de eliminar la primera empresa:", it_companies)

# 22. Eliminar la(s) empresa(s) del medio
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    del it_companies[middle_index-1:middle_index+1]
else:
    del it_companies[middle_index]
print("Lista después de eliminar la(s) empresa(s) del medio:", it_companies)

# 23. Eliminar la última empresa
it_companies.pop(-1)
print("Lista después de eliminar la última empresa:", it_companies)

# 24. Eliminar todas las empresas de la lista
it_companies.clear()
print("Lista después de eliminar todas las empresas:", it_companies)

# 25. Destruir la lista
del it_companies
# print(it_companies) # Esto causará un error porque la lista ya no existe.

# 26. Unir listas front_end y back_end
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print("Full Stack:", full_stack)

# 27. Copiar la lista y añadir Python y SQL después de Redux
full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Redux") + 2, "SQL")
print("Full Stack actualizado:", full_stack)

#NIVEL 2

# 1. Lista de edades
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# - Ordenar la lista y encontrar la edad mínima y máxima
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print("Edades ordenadas:", ages)
print("Edad mínima:", min_age)
print("Edad máxima:", max_age)

# - Agregar la edad mínima y máxima nuevamente a la lista
ages.extend([min_age, max_age])
print("Lista después de añadir min y max nuevamente:", ages)

# - Encontrar la edad mediana
ages.sort()  # Asegurarse de que la lista esté ordenada después de los cambios
if len(ages) % 2 == 0:
    median_age = (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2
else:
    median_age = ages[len(ages) // 2]
print("Edad mediana:", median_age)

# - Encontrar la edad promedio
average_age = sum(ages) / len(ages)
print("Edad promedio:", average_age)

# - Encontrar el rango de edades
age_range = max_age - min_age
print("Rango de edades:", age_range)

# - Comparar (min - promedio) y (max - promedio) usando abs()
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print("(min - promedio):", min_diff)
print("(max - promedio):", max_diff)

# 2. Encontrar los países del medio
countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas",
    "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize",
    "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil"
    # (La lista continúa en el archivo de datos.)
]
# Encontrar el/los país(es) del medio
countries.sort()  # Ordenar alfabéticamente si es necesario
middle_index = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[middle_index - 1: middle_index + 1]
else:
    middle_countries = [countries[middle_index]]
print("País(es) del medio:", middle_countries)

# 3. Dividir la lista de países en dos listas iguales
half = len(countries) // 2
if len(countries) % 2 == 0:
    first_half = countries[:half]
    second_half = countries[half:]
else:
    first_half = countries[:half + 1]
    second_half = countries[half + 1:]
print("Primera mitad:", first_half)
print("Segunda mitad:", second_half)

# 4. Desempaquetar la lista de países en 'China', 'Russia', 'USA' y los escandinavos
countries_list = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
first, second, third, *scandic_countries = countries_list
print("Primeros tres países:", first, second, third)
print("Países escandinavos:", scandic_countries)