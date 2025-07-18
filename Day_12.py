import random
import string

# --- Nivel 1 ---

# Generar un user ID aleatorio de 6 caracteres (letras y números)
def random_user_id():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

# Generar IDs según entradas del usuario
def user_id_gen_by_user():
    length = int(input("Número de caracteres para cada ID: "))
    count = int(input("Número de IDs a generar: "))
    chars = string.ascii_letters + string.digits
    for _ in range(count):
        print(''.join(random.choice(chars) for _ in range(length)))

# Generar color RGB aleatorio en formato "rgb(r,g,b)"
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

# --- Nivel 2 ---

# Generar lista de colores hexadecimales
def list_of_hexa_colors(n):
    hex_chars = string.hexdigits[:16].lower()  # '0123456789abcdef'
    colors = []
    for _ in range(n):
        color = '#' + ''.join(random.choice(hex_chars) for _ in range(6))
        colors.append(color)
    return colors

# Generar lista de colores RGB
def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]

# Generar colores hex o rgb
def generate_colors(color_type, n):
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return []

# --- Nivel 3 ---

# Barajar una lista y devolverla
def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

# Generar lista de 7 números únicos entre 0 y 9
def unique_random_numbers():
    return random.sample(range(10), 7)


# Ejemplos de uso:

if __name__ == "__main__":
    print("Random user ID:", random_user_id())
    # Para usar user_id_gen_by_user, descomenta la siguiente línea y ejecuta
    # user_id_gen_by_user()

    print("RGB color:", rgb_color_gen())
    print("Lista de 3 colores hexadecimales:", list_of_hexa_colors(3))
    print("Lista de 3 colores RGB:", list_of_rgb_colors(3))
    print("Generar 3 colores hexa con generate_colors:", generate_colors('hexa', 3))
    print("Generar 3 colores rgb con generate_colors:", generate_colors('rgb', 3))
    print("Lista original:", [1,2,3,4,5])
    print("Lista barajada:", shuffle_list([1,2,3,4,5]))
    print("7 números aleatorios únicos del 0 al 9:", unique_random_numbers())
