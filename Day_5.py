# Level 1

# 1. Lista vacía
empty_list = []

# 2. Lista con más de 5 elementos
my_list = ['apple', 'banana', 'mango', 'orange', 'grape', 'pineapple']

# 3. Longitud
print("Longitud de la lista:", len(my_list))

# 4. Primer, medio y último elemento
print("Primer elemento:", my_list[0])
print("Elemento del medio:", my_list[len(my_list) // 2])
print("Último elemento:", my_list[-1])

# 5. Datos mixtos
mixed_data_types = ['Rafael', 25, 1.75, 'Single', 'Mexico']

# 6. Lista it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Imprimir lista
print("Compañías:", it_companies)

# 8. Número de compañías
print("Número de compañías:", len(it_companies))

# 9. Primer, medio y último elementos
print("Primera compañía:", it_companies[0])
print("Compañía del medio:", it_companies[len(it_companies) // 2])
print("Última compañía:", it_companies[-1])

# 10. Modificar compañía
it_companies[0] = 'Meta'

# 11. Agregar compañía
it_companies.append('Intel')

# 12. Insertar en el medio
it_companies.insert(len(it_companies) // 2, 'Adobe')

# 13. Convertir a mayúsculas (IBM excluido)
it_companies = [comp.upper() if comp != 'IBM' else comp for comp in it_companies]

# 14. Unir con separador
print("#; ".join(it_companies))

# 15. Verificar si existe una compañía
print("¿GOOGLE está en la lista?", 'GOOGLE' in it_companies)

# 16. Ordenar
it_companies.sort()
print("Ordenadas:", it_companies)

# 17. Reverso
it_companies.reverse()
print("Reverso:", it_companies)

# 18. Primeros 3
print("Primeros 3:", it_companies[:3])

# 19. Últimos 3
print("Últimos 3:", it_companies[-3:])

# 20. Medio
mid = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    print("Del medio:", it_companies[mid-1:mid+1])
else:
    print("Del medio:", [it_companies[mid]])

# 21. Eliminar primero
it_companies.pop(0)

# 22. Eliminar medio
mid = len(it_companies) // 2
it_companies.pop(mid)

# 23. Eliminar último
it_companies.pop()

# 24. Limpiar lista
it_companies.clear()

# 25. Destruir lista
del it_companies

# 26. Unir front_end y back_end
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end

# 27. Insertar Python y SQL después de Redux
index = full_stack.index('Redux')
full_stack[index + 1:index + 1] = ['Python', 'SQL']
print("Full stack final:", full_stack)

# Level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = min(ages)
max_age = max(ages)
ages.append(min_age)
ages.append(max_age)

# Mediana
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median_age = ages[n//2]
print("Mediana:", median_age)

# Promedio
average_age = sum(ages) / len(ages)
print("Promedio:", average_age)

# Rango
print("Rango:", max_age - min_age)

# Diferencia con promedio
print("abs(min - promedio):", abs(min_age - average_age))
print("abs(max - promedio):", abs(max_age - average_age))

# Países
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_index = len(countries) // 2
if len(countries) % 2 == 0:
    print("Países del medio:", countries[middle_index - 1:middle_index + 1])
else:
    print("País del medio:", countries[middle_index])

# Dividir lista
first_half = countries[:(len(countries)+1)//2]
second_half = countries[(len(countries)+1)//2:]
print("Primera mitad:", first_half)
print("Segunda mitad:", second_half)

# Desempaquetar
china, russia, usa, *scandic_countries = countries
print("Scandic countries:", scandic_countries)
