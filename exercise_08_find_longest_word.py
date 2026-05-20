# Ejercicio 8 - Palabra más larga de un archivo


def find_longest_word(filename):
    """
    Lee el archivo, lo divide en palabras (separadas por cualquier tipo
    de whitespace) y retorna la palabra más larga.

    Reglas:
    - Si hay varias palabras con la misma longitud máxima, retornar la
      PRIMERA en aparecer.
    - Si el archivo no existe, propagar FileNotFoundError.
    - Si el archivo no tiene ninguna palabra (está vacío o solo tiene
      espacios/saltos de línea), lanzar ValueError("file has no words").

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        str - la palabra más larga del archivo.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si el archivo no tiene palabras.

    Ejemplo:
        # archivo contiene: "el gato corre rapido\npor el jardin\n"
        find_longest_word("texto.txt") -> "rapido"
    """
    try:
        with open(filename, "r") as archivo:
            lineas = [line.strip().split() for line in archivo]
            #print(lineas)
            cant_char = {}
            max_len = -1
            empty_list = True
            for line in lineas:
                #print(line)
                for word in line:
                    if word not in cant_char:
                        cant_char[word] = len(word)
                    if len(word) > max_len:
                        max_len = len(word)
                        #print(max_len)
                        empty_list = False
            for key, value in cant_char.items():
                if value == max_len:
                    return key
            if empty_list:
                raise ValueError("file has no words")
    except FileNotFoundError:
        raise FileNotFoundError
