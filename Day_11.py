import math
from collections import Counter
import keyword

# --------- Nivel 1 ---------

# 1. Sumar dos números
def add_two_numbers(a, b):
    return a + b

# 2. Área de un círculo
def area_del_circulo(r):
    return math.pi * r * r

# 3. Sumar números arbitrarios
def add_all_nums(*args):
    if all(isinstance(x, (int, float)) for x in args):
        return sum(args)
    else:
        return "Todos los elementos deben ser números"

# 4. Convertir Celsius a Fahrenheit
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# 5. Determinar estación según mes
def check_season(month):
    month = month.capitalize()
    if month in ['September', 'October', 'November']:
        return 'Otoño'
    elif month in ['December', 'January', 'February']:
        return 'Invierno'
    elif month in ['March', 'April', 'May']:
        return 'Primavera'
    elif month in ['June', 'July', 'August']:
        return 'Verano'
    else:
        return 'Mes inválido'

# 6. Calcular pendiente entre dos puntos
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Pendiente indefinida (división por cero)"
    return (y2 - y1) / (x2 - x1)

# 7. Solución de ecuación cuadrática
def solve_quadratic_eqn(a, b, c):
    d = b**2 - 4*a*c  # discriminante
    if d < 0:
        return "Raíces complejas"
    elif d == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return (x1, x2)

# 8. Imprimir elementos de una lista
def print_list(lst):
    for item in lst:
        print(item)

# 9. Invertir lista usando bucle
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

# 10. Capitalizar elementos de lista
def capitalize_list_items(lst):
    return [str(item).upper() for item in lst]

# 11. Añadir elemento a lista
def add_item(lst, item):
    lst.append(item)
    return lst

# 12. Remover elemento de lista
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# 13. Sumar números en rango
def sum_of_numbers(n):
    return sum(range(1, n+1))

# 14. Sumar números impares en rango
def sum_of_odds(n):
    return sum(i for i in range(1, n+1) if i % 2 != 0)

# 15. Sumar números pares en rango
def sum_of_evens(n):
    return sum(i for i in range(1, n+1) if i % 2 == 0)


# --------- Nivel 2 ---------

# 16. Contar pares e impares
def evens_and_odds(n):
    evens = sum(1 for i in range(n+1) if i % 2 == 0)
    odds = sum(1 for i in range(n+1) if i % 2 != 0)
    print(f"The number of odds are {odds}.")
    print(f"The number of evens are {evens}.")

# 17. Factorial
def factorial(n):
    if n < 0:
        return "No definido para números negativos"
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# 18. Verificar si vacío
def is_empty(value):
    return len(value) == 0 if hasattr(value, '__len__') else False

# 19. Funciones estadísticas para lista
def mean(lst):
    return sum(lst)/len(lst) if lst else 0

def median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid -1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def mode(lst):
    c = Counter(lst)
    max_count = max(c.values())
    return [k for k,v in c.items() if v == max_count]

def data_range(lst):
    return max(lst) - min(lst) if lst else 0

def variance(lst):
    m = mean(lst)
    return sum((x - m)**2 for x in lst) / len(lst) if lst else 0

def std_deviation(lst):
    return math.sqrt(variance(lst))

# --------- Nivel 3 ---------

# 20. Verificar número primo
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# 21. Verificar elementos únicos
def all_unique(lst):
    return len(lst) == len(set(lst))

# 22. Verificar si todos son mismo tipo
def all_same_type(lst):
    if not lst:
        return True
    t = type(lst[0])
    return all(isinstance(x, t) for x in lst)

# 23. Verificar si es nombre válido de variable Python
def is_valid_variable(name):
    return name.isidentifier() and not keyword.iskeyword(name)

# 24 y 25 (sobre datos externos):
# Aquí debes cargar los datos de Countries-data.py para implementar estas funciones,
# por ahora te dejo estructura simple:

def top_spoken_languages(data, top=10):
    languages = []
    for country in data:
        languages.extend(country.get('languages', []))
    c = Counter(languages)
    return c.most_common(top)

def top_populated_countries(data, top=10):
    sorted_countries = sorted(data, key=lambda x: x.get('population', 0), reverse=True)
    return sorted_countries[:top]


# Ejemplo uso de funciones nivel 1
if __name__ == "__main__":
    print(add_two_numbers(3, 4))
    print(area_del_circulo(5))
    print(add_all_nums(1, 2, 3, 4))
    print(add_all_nums(1, 'a', 3))  # No numérico
    print(convert_celsius_to_fahrenheit(0))
    print(check_season("March"))
    print(calculate_slope(1, 2, 3, 4))
    print(solve_quadratic_eqn(1, -3, 2))
    print_list(['a', 'b', 'c'])
    print(reverse_list([1, 2, 3]))
    print(capitalize_list_items(['a', 'b', 'c']))
    print(add_item([1, 2], 3))
    print(remove_item([1, 2, 3], 2))
    print(sum_of_numbers(5))
    print(sum_of_odds(10))
    print(sum_of_evens(10))
    evens_and_odds(10)
    print(factorial(5))
    print(is_empty([]))
    print(mean([1,2,3]))
    print(median([1,2,3,4]))
    print(mode([1,1,2,2,3]))
    print(data_range([1,2,3]))
    print(std_deviation([1,2,3]))
    print(is_prime(7))
    print(all_unique([1,2,3]))
    print(all_same_type([1,2,3]))
    print(is_valid_variable("var1"))