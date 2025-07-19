# Nivel 3

# Países con 'land'
countries = ["Finland", "Iceland", "Thailand", "Poland", "Switzerland", "Ireland", "England", "Netherlands"]
land_countries = [c for c in countries if 'land' in c.lower()]
print("Países con 'land':", land_countries)

# Invertir lista de frutas
fruits = ['banana', 'naranja', 'mango', 'limón']
reversed_fruits = []
for i in range(len(fruits)-1, -1, -1):
    reversed_fruits.append(fruits[i])
print("Frutas invertidas:", reversed_fruits)

# Datos simulados para idiomas y población
countries_data = [
    {'country': 'China', 'languages': ['Mandarin'], 'population': 1409517397},
    {'country': 'India', 'languages': ['Hindi', 'English'], 'population': 1339180127},
    {'country': 'USA', 'languages': ['English'], 'population': 324459463},
    {'country': 'Indonesia', 'languages': ['Indonesian'], 'population': 263991379},
    {'country': 'Brazil', 'languages': ['Portuguese'], 'population': 209288278},
    {'country': 'Pakistan', 'languages': ['Urdu', 'English'], 'population': 197015955},
    {'country': 'Nigeria', 'languages': ['English'], 'population': 190886311},
    {'country': 'Bangladesh', 'languages': ['Bengali'], 'population': 164669751},
    {'country': 'Russia', 'languages': ['Russian'], 'population': 143989754},
    {'country': 'Mexico', 'languages': ['Spanish'], 'population': 129163276},
]

# Total idiomas
all_languages = set()
for c in countries_data:
    for lang in c['languages']:
        all_languages.add(lang)
print("Total idiomas:", len(all_languages))

# Top 10 idiomas más hablados (por cantidad de países que lo hablan)
lang_count = {}
for c in countries_data:
    for lang in c['languages']:
        lang_count[lang] = lang_count.get(lang, 0) + 1

top_languages = sorted(lang_count.items(), key=lambda x: x[1], reverse=True)[:10]
print("Top idiomas:")
for lang, count in top_languages:
    print(lang, "-", count)

# Top 10 países más poblados
top_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]
print("Top países por población:")
for c in top_countries:
    print(c['country'], "-", c['population'])