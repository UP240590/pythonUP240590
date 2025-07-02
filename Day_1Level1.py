#ejercicio 1

print(3 + 4)         #addition(+)
print(3 - 4)         #substraction(-)
print(3 * 4)         #multiplication(*)
print(3 / 4)         #division(/)
print(3 ** 4)        #exponential(**)
print(3 % 4)         #moduls(%)
print(3 // 4)        #Floor division operator (//)

#ejercicio 2

print("Rafael")
print("Romo")
print("México")
print("I am enjoying 30 days of paython")

#ejercicio 3

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh','Python','Finland']))
print(type("Rafael"))
print(type("Rafael, María, Laura, Veronica, Areli"))
print(type("México"))

#Ejercicio1_Nivel 3

print(type({'name':'Rafael'}))          #Dictionary
print(type({9.8, 3.14, 2.7}))           #set
print(type((9.8, 3.14, 2.7)))           #Tuple

import math
def distancia_euclidiana(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Puntos datos
Punto1 = (2, 3)
Punto2 = (10, 8)

# Calcular distancia
distancia = distancia_euclidiana(Punto1[0], Punto1[1], Punto2[0], Punto2[1])
print(f"Punto 1:{Punto1}")
print(f"Punto 2: {Punto2}")
print(f"Distancia Euclidiana: {distancia:.2f}")
