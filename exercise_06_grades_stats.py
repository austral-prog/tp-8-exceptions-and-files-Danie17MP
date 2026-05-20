# Ejercicio 6 - Estadísticas de notas por estudiante
import os

def grades_stats(filename):
    """
    Lee un archivo donde cada línea tiene el formato:

        estudiante:nota1,nota2,nota3,...

    y retorna un diccionario donde la clave es el nombre del estudiante y
    el valor es una TUPLA (promedio, maximo, minimo) con los tres valores
    como float.

    Reglas:
    - El promedio se calcula con todas las notas de la línea.
    - Las líneas vacías se ignoran.
    - Se garantiza que todas las notas son números válidos.
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, tuple[float, float, float]] - estadísticas por estudiante.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "Ana:8,9,7\nBeto:5,5,10\nCami:10\n"
        grades_stats("notas.txt") -> {
            "Ana": (8.0, 9.0, 7.0),
            "Beto": (6.666666666666667, 10.0, 5.0),
            "Cami": (10.0, 10.0, 10.0),
        }
    """
    if not os.path.exists(filename):
        raise FileNotFoundError("Archivo no existe")

    with open(filename, "r") as file:
        final_dictio = {}
        alum_and_notes = [line.split(":") for line in file if line != "\n" or ""]
        cant_alum = len(alum_and_notes)
        alum_names = [alum_and_notes[i][0] for i in range(cant_alum)]
        alum_notes = [alum_and_notes[i][1].split(",") for i in range(cant_alum)]
        alum_notes = [[float(note) for note in notes] for notes in alum_notes]
        for i in range(cant_alum):
            suma = sum(alum_notes[i])
            promedio = suma / len(alum_notes[i])
            maximo = max(alum_notes[i])
            minimo = min(alum_notes[i])
            tuple_notes = (promedio, maximo, minimo)
            final_dictio[alum_names[i]] = tuple_notes
    return final_dictio
