
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
