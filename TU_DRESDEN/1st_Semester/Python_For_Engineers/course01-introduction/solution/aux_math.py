"""
Diese Python-Datei ist nicht zum direkten ausführen vorgessehen.
Sie sollte mit `import aux_math` importiert werden.
"""


def is_number(string):
    """
    testet ob der string ohne fehlermeldung in eine Zahl umgewandelt werden
    kann
    """

    try:
        float(string)
    except ValueError:
        # Fehler -> keine Zahl
        return False

    # Kein Fehler -> Zahl
    return True
