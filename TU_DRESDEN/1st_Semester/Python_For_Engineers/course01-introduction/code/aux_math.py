"""
This Python file is not intended to be executed directly.
It should be imported with `import aux_math`.
"""


def is_number(string):
    """
    tests if the string can be converted to a number without error message
    """

    try:
        float(string)
    except ValueError:
        # Fehler -> keine Zahl
        return False

    # Kein Fehler -> Zahl
    return True
