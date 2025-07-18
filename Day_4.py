# Concatenaciones

string1 = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(string1)  # 'Thirty Days Of Python'

string2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(string2)  # 'Coding For All'
company = "Coding For All"
print(company)       # 'Coding For All'
print(len(company))       # Longitud de la cadena
print(company.upper())    # Mayúsculas
print(company.lower())      # Minúsculas
print(company.capitalize())    # Capitaliza
print(company.title())        # Título
print(company.swapcase())   # Invierte mayúsculas/minúsculas 

print(company[0:6])                # 'Coding' (primer palabra)

print(company.find("Coding"))     # Encuentra 'Coding' → 0
print(company.index("Coding"))    # También devuelve 0

print(company.replace("Coding", "Python"))  # 'Python For All'

print("Python for Everyone".replace("Everyone", "All"))  # 'Python for All'
print(company.split())  # ['Coding', 'For', 'All']

tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(", "))  # Divide por coma

print(company[0])                  # Caracter en el índice 0 → 'C'
print(len(company) - 1)            # Último índice → 13
print(company[10])                 # Índice 10 → 'r'
phrase1 = "Python For Everyone"
acronym1 = ''.join([word[0] for word in phrase1.split()])
print(acronym1)  # 'PFE'

phrase2 = "Coding For All"
acronym2 = ''.join([word[0] for word in phrase2.split()])
print(acronym2)  # 'CFA'
print(company.index("C"))     # 0
print(company.index("F"))     # 7

long_string = "Coding For All People"
print(long_string.rfind("l"))  # Última 'l' → posición 17

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))       # 31
print(sentence.rindex("because"))     # 47

# Extraer 'because because because'
start = sentence.find("because")
end = sentence.rindex("because") + len("because")
print(sentence[start:end])            # 'because because because'

print(company.startswith("Coding"))  # True
print(company.endswith("coding"))    # False

trimmed = '   Coding For All      '.strip()
print(trimmed)                       # 'Coding For All'

# isidentifier()
print("30DaysOfPython".isidentifier())          # False
print("thirty_days_of_python".isidentifier())   # True


libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libs))  # 'Django # Flask # Bottle # Pyramid # Falcon'

# Nueva línea
print("I am enjoying this challenge.\nI just wonder what is next.")

# Tabulación
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.0f} meters square.".format(radius, area))

a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} * {} = {}".format (a, b, a * b))