import itertools

# Definimos los elementos a combinar
elements = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Definimos el tamaño máximo de cada combinación
combination_length = 4

# Abrimos el archivo en modo de escritura
with open('./dictionaries/All/RockLliu.txt', 'w') as file:

    # Generamos todas las posibles combinaciones
    combinations = itertools.product(elements, repeat=combination_length)

    # Escribimos las combinaciones en el archivo
    for combination in combinations:
        file.write(''.join(combination) + '\n')
