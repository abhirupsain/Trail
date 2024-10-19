"""
show docstrings
"""


funcs = [bin, hex, oct, ord, chr, int]


for f in funcs:
    print(f.__name__)
    print(f.__doc__)
    print("-"*10, "\n")
