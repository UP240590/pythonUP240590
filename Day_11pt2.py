# --------- Nivel 2 ---------

import math
from collections import Counter

# 16. Contar pares e impares
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = sum(1 for i in range(n + 1) if i % 2 != 0)
    print(f"The number of odds are {odds}.")
    print(f"The number of evens are {evens}.")

# 17. Factorial
def factorial(n):
    if n < 0:
        return "No definido para números negativos"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 18. Verificar si está vacío
def is_empty(value):
    return len(value) == 0 if hasattr(value, '__len__') else False

# 19. Funciones estadísticas para lista
def mean(lst):
    return sum(lst) / len(lst) if lst else 0

def median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def mode(lst):
    c = Counter(lst)
    max_count = max(c.values())
    return [k for k, v in c.items() if v == max_count]

def data_range(lst):
    return max(lst) - min(lst) if lst else 0

def variance(lst):
    m = mean(lst)
    return sum((x - m) ** 2 for x in lst) / len(lst) if lst else 0

def std_deviation(lst):
    return math.sqrt(variance(lst))
