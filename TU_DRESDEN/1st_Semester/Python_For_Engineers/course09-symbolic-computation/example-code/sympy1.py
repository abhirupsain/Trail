import sympy as sp
x = sp.Symbol("x")
a, b, c = sp.symbols("a b c")  # different ways to create symbols

z = a*b*x*b + b**2*a*x - c*b*(2*a/c*x*b-1/(b*2))
print(z)  # -> -b*c*(-1/(2*b) + 2*a*b*x/c) + 2*a*x*b**2
print(z.expand())  # -> c/2 (multiply out)

# apply functions:
y = sp.sin(x)*sp.exp(3*x)*sp.sqrt(a)
print(y)  # -> a**(1/2)*exp(x)*sin(x)

# define custom function
f1 = sp.Function("f")  # -> sympy.core.function.f (not evaluated)
g1 = sp.Function("g")(x)  # -> g(x)    (function evaluated at x)

# taking derivatives
print(y.diff(x))  # -> 3*sqrt(a)*exp(3*x)*sin(x) + sqrt(a)*exp(3*x)*cos(x)
print(g1.diff(x))  # -> Derivative(g(x), x)

# simplification (example):
y = sp.sin(x)**2+sp.cos(x)**2)
print(y == 1)  # -> False
print(sp.simplify(y))  # -> 1
print(sp.simplify(y) == 1)  # -> True
