# Crear una tupla vacía
empty_tuple = ()

# Crear una tupla con nombres de hermanas y hermanos
sisters = ('Laura', 'Veronica', 'Areli')
brothers = ()  # No se mencionaron hermanos, así que está vacía

# Unir las tuplas de hermanas y hermanos
siblings = sisters + brothers

# Contar cuántos hermanos en total
print("Número de hermanos:", len(siblings))

# Agregar a mamá y papá a la tupla de hermanos
family_members = siblings + ('Maria de Lourdes', 'Rafael')

# Desempaquetar hermanos y padres de la tupla family_members
*siblings_only, mother, father = family_members

# Mostrar miembros de la familia
print("Hermanos(as):", siblings_only)
print("Mamá:", mother)
print("Papá:", father)

# Crear tuplas de frutas, verduras y productos animales
fruits = ('Mango', 'Kiwi')
vegetables = ('Papa', 'Brócoli')
animal_products = ('Huevo', 'Queso')

# Unir las tres tuplas en una sola
all_foods_tuple = fruits + vegetables + animal_products

# Convertir la tupla a lista
all_foods_list = list(all_foods_tuple)

# Sacar el ítem o ítems del medio
middle_index = len(all_foods_list) // 2
if len(all_foods_list) % 2 == 0:
    middle_items = all_foods_list[middle_index - 1:middle_index + 1]
else:
    middle_items = [all_foods_list[middle_index]]

print("Elemento(s) del medio:", middle_items)

# Sacar los primeros tres y últimos tres elementos
first_three = all_foods_list[:3]
last_three = all_foods_list[-3:]

print("Primeros tres alimentos:", first_three)
print("Últimos tres alimentos:", last_three)

# Eliminar completamente la tupla all_foods_tuple (opcional)
# del all_foods_tuple  # Solo si ya no la necesitas

# Verificar si un ítem está en una tupla de países nórdicos
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('¿Estonia está en países nórdicos?', 'Estonia' in nordic_countries)  # False
print('¿Iceland está en países nórdicos?', 'Iceland' in nordic_countries)  # True