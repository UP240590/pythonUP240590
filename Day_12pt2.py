# --- Nivel 2 ---

import random
import string

# Generar un solo color RGB
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"

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
