# --------- Nivel 3 ---------

import math
import keyword
from collections import Counter

# 20. Verificar número primo
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 21. Verificar elementos únicos
def all_unique(lst):
    return len(lst) == len(set(lst))

# 22. Verificar si todos son del mismo tipo
def all_same_type(lst):
    if not lst:
        return True
    t = type(lst[0])
    return all(isinstance(x, t) for x in lst)

# 23. Verificar si es nombre válido de variable Python
def is_valid_variable(name):
    return name.isidentifier() and not keyword.iskeyword(name)

# 24. Top lenguajes más hablados (requiere datos)
def top_spoken_languages(data, top=10):
    languages = []
    for country in data:
        languages.extend(country.get('languages', []))
    c = Counter(languages)
    return c.most_common(top)

# 25. Países más poblados (requiere datos)
def top_populated_countries(data, top=10):
    sorted_countries = sorted(data, key=lambda x: x.get('population', 0), reverse=True)
    return sorted_countries[:top]


