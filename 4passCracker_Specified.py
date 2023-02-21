import itertools

# Definimos los elementos a combinar
elements = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Definimos el tamaño máximo de cada combinación
combination_length = 4

# Creamos un diccionario para almacenar los archivos
files_dict = {}
for char in elements:
    if char.isdigit():
        files_dict[char] = open(f"dictionaries/Numbers/numbers.txt", "a")
    else:
        files_dict[char] = open(f"dictionaries/Letters/{char.lower()}.txt", "a")

# Generamos todas las posibles combinaciones
combinations = itertools.product(elements, repeat=combination_length)

# Escribimos las combinaciones en los archivos correspondientes
for combination in combinations:
    key = combination[0]
    file = files_dict[key]
    file.write(''.join(combination) + '\n')

# Cerramos todos los archivos
for file in files_dict.values():
    file.close()