# Ejercicio 4 - Promedio seguro con manejo de errores
import os

def safe_average(filename):
    """
    Lee un archivo donde hay UN número por línea y retorna el promedio de
    los números válidos (como float).

    Reglas:
    - Las líneas que no se puedan convertir a float deben ignorarse (usar
      try/except ValueError internamente).
    - Las líneas vacías también se ignoran.
    - Si el archivo no existe, propagar FileNotFoundError.
    - Si el archivo existe pero no contiene ningún número válido, lanzar
      ValueError("no valid numbers").

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        float - promedio de los números válidos.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si no hay números válidos en el archivo.

    Ejemplo:
        # archivo contiene: "10\n20\nno_es_un_numero\n30\n"
        safe_average("numeros.txt") -> 20.0
    """
    if not os.path.exists(filename):
        raise FileNotFoundError("no existe sete archivo")

    sum_avg = 0.0
    invalid_archivo = True
    valid_nums = 0
    with open(filename, "r") as archivo:
        for num in archivo:
            try:
                num = float(num)
                sum_avg += num
                invalid_archivo = False
                valid_nums += 1
            except ValueError:
                pass
    if invalid_archivo:
        raise ValueError("no valid numbers")
    else:
        return sum_avg / valid_nums
