#1 Declare you age as integrer variable
import math


age=21

#2 Declare your height as a float variable 
height=1.66

#3 Declare a variable that stores a comlpe x number
complex_number=3+4j

print("Age:", age);
print("Height:", height);
print("Complex Number:",complex_number);
print("-"*50);

#4 Triangle area calculation

base=float(input("Ingrese la base: "))
height=float(input("Ingrese la altura: "))
area=0.5*base*height
print("El area del triangulo es:", area);
print("-"*50);

#5 Triangle Perimeter calculation

side_a=float(input("Introduce el lado a:"))
side_b=float(input("Introduce el lado b:"))
side_c=float(input("Introduce el lado c:"))
perimeter=side_a+side_b+side_c
print("El perimetro del triangulo es: ", perimeter)
print("-"*50);

#6 Rectangle area and perimeter

length=float(input("Introduce la longitud del rectangulo:"))
Width=float(input("Introduce el ancho del rectangulo:"))
area=length*Width
perimeter= 2*(length+Width)
print("El area es:", area)
print("El perimetro es:", perimeter)
print("-"*50);

#7Circle area and circunference

radio= float(input("Introduce el radio del circulo:"))
pi=3.14
area= pi* radio * radio
circunference = 2 * pi * radio
print("Area:", area)
print("Circunferencia:", circunference)
print("-"*50);

#8 Calculate slope, x-intercept and y-interecept of y= 2x-2
#For y = 2x-2
   #slope (m)=2
   #Y-intercept: when x = 0, y = -2
   #X-intercept: when y = 0, 0=2x-2, so x = 1
slope=2
y_intercept=-2
x_intercept=1

print("Para la ecuacion y=2x-2:")
print("slope:", slope)
print("Intercepcion Y:",y_intercept)
print("Intercepcion X:",x_intercept)
print("-"*50)

#9 Slope and Euclidean distance between two points
# Points: (2, 2) and (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10

# Slope calculation
slope = (y2 - y1) / (x2 - x1)
# Euclidean distance
distance = math.sqrt((x2 - x1)*2 + (y2 - y1)*2)
print(f"Entre puntos ({x1}, {y1}) and ({x2}, {y2}):")
print(f"Slope: {slope}")
print("Distancia Euclideana:",distance)
print("-"*50);

# 10. Compare slopes from tasks 8 and 9
    # Pendiente del ejercicio 8 (y = 2x - 2)
slope_task8 = 2

    # Pendiente del ejercicio 9 (puntos (2,2) y (6,10))
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_task9 = (y2 - y1) / (x2 - x1)

print(f"Pendiente ejercicio 8: {slope_task8}")
print(f"Pendiente ejercicio 9: {slope_task9}")
print(f"¿Son iguales? {slope_task8 == slope_task9}")
print("-"*50);

# 11. Quadratic equation y = x^2 + 6x + 9
x_values = [-5, -4, -3, -2, -1, 0, 1]

for x in x_values:
    y = x**2 + 6*x + 9
    print(f"Cuando x = {x}, y = {y}")

print("y = 0 cuando x = -3")
print("-"*50);

# 12. String comparisons and operations
python_len = len('python')
dragon_len = len('dragon')

print(f"Longitud de 'python': {python_len}")
print(f"Longitud de 'dragon': {dragon_len}")
print(f"¿'python' y 'dragon' tienen la misma longitud? {python_len == dragon_len}")
print("-"*50);

# 13. Check if 'on' is in both 'python' and 'dragon'
python_has_on = 'on' in 'python'
dragon_has_on = 'on' in 'dragon'
both_have_on = python_has_on and dragon_has_on

print(f"'on' está en 'python': {python_has_on}")
print(f"'on' está en 'dragon': {dragon_has_on}")
print(f"'on' está en ambos 'python' y 'dragon': {both_have_on}")
print("-"*50);

# 14. Check if 'jargon' is in sentence
sentence = "I hope this course is not full of jargon"
has_jargon = 'jargon' in sentence
print(f"Oración: '{sentence}'")
print(f"¿'jargon' está en la oración? {has_jargon}")
print("-"*50);

# 15. Statement about 'on' in dragon and python
print("Declaración: 'No hay 'on' en dragon y python'")
print(f"Esta declaración es: {not ('on' in 'dragon' and 'on' in 'python')}")
print("(La declaración es falsa porque 'python' sí contiene 'on')")
print("-"*50);

# 16. Convert string operations
text = 'python'
length = len(text)
length_float = float(length)
length_string = str(length_float)

print(f"Texto: '{text}'")
print(f"Longitud: {length}")
print(f"Longitud como float: {length_float}")
print(f"Longitud como string: '{length_string}'")
print(f"Tipo de length: {type(length)}")
print(f"Tipo de length_float: {type(length_float)}")
print(f"Tipo de length_string: {type(length_string)}")
print("-"*50);

# 17. Check if number is even

number = 10
is_even = number % 2 == 0
print(f"{number} es par: {is_even}")

number2 = 7 # Ejemplo con otro número
is_even2 = number2 % 2 == 0
print(f"{number2} es par: {is_even2}")

print("-"*50);

# 18. Floor division check
floor_div = 7 // 3
int_converted = int(2.7)
print(f"7 // 3 = {floor_div}")
print(f"int(2.7) = {int_converted}")
print(f"Son iguales? {floor_div == int_converted}")
print("-"*50);

# 19. Type comparison

type1 = type('10')
type2 = type(10)

print(f"type('10'): {type1}")
print(f"type(10): {type2}")
print(f"Son iguales? {type1 == type2}")
print("-"*50);

# 20. Int conversion check
try:
    result = int('9.8')
    print(f"int('9.8') = {result}")
    print(f"int('9.8') == 10: {result == 10}")
except ValueError as e:
    print(f"Error: {e}")
    print("int('9.8') generará un ValueError porque '9.8' no es una cadena entera válida")
print("-"*50);

# 21. Pay calculator
hours = float(input("Introduce las horas: "))
rate = float(input("Introduzca la tarifa por hora: "))
pay = hours * rate
print("Tus ganancias semanales son:",pay)
print("-"*50);

# 22. Seconds lived calculator
years = int(input("Introduce cuantos años tienes: "))
seconds_per_year = 365 * 24 * 60 * 60  # 31,536,000 segundos por año
total_seconds = years * seconds_per_year
print("Haz vivido por ",total_seconds," segundos")
print("-"*50);

# 23. Display table
print("\nTable display:")
for i in range(1, 6):
        print(f"{i} 1 {i} {i*2} {i*3}")



