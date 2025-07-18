# Filtrar negativos y ceros usando comprensión de listas
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives_and_zeros = [num for num in numbers if num <= 0]
print("Negativos y ceros:", negatives_and_zeros)

# Aplanar lista de listas de listas a lista unidimensional
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2]
print("Lista aplanada:", flattened)

# Crear lista de tuplas usando comprensión de listas
tuples_list = [
    (i, 1, i, i**2, i**3, i**4, i**5)
    for i in range(11)
]
print("Lista de tuplas:")
for t in tuples_list:
    print(t)

# Aplanar lista countries y crear nueva lista con abreviaturas y mayúsculas
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
processed_countries = [
    [country[0].upper(), country[0][:3].upper(), country[1].upper()]
    for sublist in countries
    for country in sublist
]
print("Países procesados:", processed_countries)

# Convertir lista a lista de diccionarios
countries_dicts = [
    {'country': country[0].upper(), 'city': country[1].upper()}
    for sublist in countries
    for country in sublist
]
print("Lista de diccionarios:", countries_dicts)

# Convertir lista de nombres a lista de cadenas concatenadas
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [
    f"{name[0]} {name[1]}"
    for sublist in names
    for name in sublist
]
print("Nombres concatenados:", concatenated_names)

# Función lambda para calcular pendiente (m) de y = mx + b
calculate_slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None

# Ejemplo uso de la lambda
print("Pendiente entre (1,2) y (3,6):", calculate_slope(1, 2, 3, 6))
