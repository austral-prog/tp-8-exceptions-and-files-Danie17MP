# Ejercicio 7 - Escribir un inventario ordenado
import os

def write_inventory(filename, inventory):
    """
    Escribe el inventario en un archivo, una línea por item, ordenadas
    alfabéticamente por nombre de item, con el formato:

        item:cantidad

    Reglas:
    - Cada línea debe terminar con "\\n".
    - Si el diccionario está vacío, el archivo se crea vacío.
    - Si el archivo ya existía, se sobreescribe.
    - La función no retorna nada (None).

    Args:
        filename: str - nombre del archivo a escribir.
        inventory: dict[str, int] - item -> cantidad.

    Returns:
        None

    Ejemplo:
        write_inventory("stock.txt", {"wood": 10, "coal": 3, "iron": 7})
        # El archivo stock.txt queda con:
        # coal:3
        # iron:7
        # wood:10
    """
    if os.path.exists(filename):
        with open(filename, "w") as my_file:
            sorted(inventory.items(), key=lambda x: x[0])
            for key, value in inventory.items():
                my_file.write(f"{key}:{value}\n")
    else:
        with open(filename, "a") as my_file:
            a = sorted(inventory.items(), key = lambda x: x[0])
            for key, value in a:
                my_file.write(f"{key}:{value}\n")
    return None