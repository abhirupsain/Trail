import math; from timeit import timeit

def root1(x=2): return x**0.5

def root2(): return math.sqrt(2)

N = int(1e6)
print("2**0.5:    ", timeit("2**0.5", number=N), "sqrt(2):", timeit("math.sqrt(2)", setup="import math", number=N))

# func calls without argument
print("root1():   ", timeit(root1, number=N), "root2():", timeit(root2, number=N))

# func calls with argument (timeit(root2(x=2), number=N))) would "see" only the return value
# Thus, wee need to pass the function call as string. Then the `globals`- keyword argument is also needed.
print("root1(x=2):", timeit("root1(x=2)", number=N, globals=globals()))
