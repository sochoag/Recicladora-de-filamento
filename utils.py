def map_value(value, in_min, in_max, out_min, out_max):
    """
    Escala un valor de entrada a un rango de salida especificado.

    Args:
        value: el valor a escalar.
        in_min: el valor mínimo de la entrada.
        in_max: el valor máximo de la entrada.
        out_min: el valor mínimo de la salida.
        out_max: el valor máximo de la salida.

    Returns:
        El valor escalado a un rango de salida especificado.
    """
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min