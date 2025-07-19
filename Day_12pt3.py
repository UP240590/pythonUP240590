# --- Nivel 3 ---

import random

# Barajar una lista y devolverla
def shuffle_list(lst):
    shuffled = lst[:]          # Crea una copia para no modificar la original
    random.shuffle(shuffled)   # Baraja la copia
    return shuffled

# Generar lista de 7 números únicos entre 0 y 9
def unique_random_numbers():
    return random.sample(range(10), 7)

