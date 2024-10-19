from sympy import sin, cos, Function
import sympy as sp
import sys


## this file contains a skeleton and has to be amended
# the variable XXX is only a placeholder and has to be replaced appropriately in each case

# task 1
params = sp.symbols("m1, m2")  # incomplete (parameters are missing)
m1, m2 = params

sys.exit()  # move this line further down as you proceed with the exercise



# task 2
t = sp.Symbol("XXX")  # create the symbol for the time
xt = Function("x")(t)  # x(t)
phit = Function(XXX)(XXX)  # phi(t)

# task 3 (construct four time derivatives)
xdt = xt.diff(t)
## ...
xddt = xt.diff(t, 2)
## ...


# task 4

# auxiliary quantities
x2t = XXX
y2t = XXX

x2dt = XXX.diff(t)
## ...

# task 5
# kinetic energy
T = (m1*xdt**2 + XXX)/2

# potential energy
U = XXX

L = T - U  # Lagrange funktion

# perform simplifications of expression L
L = L.expand()
L = sp.trigsimp(L)


# --- Lagrange Equations ---

# task 6

# auxiliary expressions:
L_d_x = L.diff(xt)
L_d_phi = XXX

L_d_xd = XXX
L_d_phid = XXX

# task 7
DL_d_xd = XXX.diff(t)
DL_d_phid = XXX


# task 8
F = sp.Symbol("F")  # external force (translatoric)

# right hand side of the equations of motion (left hand side is zero)
Eq1 =  XXX - XXX - F
Eq2 =  XXX

# useful for debugging: pretty printing
# sp.pprint(Eq1)
# sp.pprint(Eq2)


# task 9
# list of accelerations
acc = [xddt, XXX]

# solve equations for acceleration symbols
res = sp.solve([XXX, XXX], acc)

# task 10

msg = f"\nThe variable `res` is of type: {XXX} and has the following value:\n"
print(msg)
sp.pprint(res)

xdd_expr = res[xddt]
phidd_expr = XXX


# task 11

# Generate Python functions for the numerical calculation of the accelerations
# This requires some preparation:
#  1. replace the t-dependent functions by normal symbols
#  2. insert numerical parameter values.

# step 1: create symbols (so far we had functions depending on t):

x, phi, xd, phid, xdd, phidd = sp.symbols("x, phi, xd, phid, xdd, phidd")

# list for replacements; in each case a 2-tuple: (t-dependent function, symbol)
# note: Substitute highest time derivatives first (accelerations)
rplmts = [(xddt, xdd), (phiddt, phidd), (xdt, xd), (phidt, phid),
          (xt, x), (phit, phi)]

# step 2:
params_values = [(m1, 0.8), XXX]


# perform subsitution and save result in variables
xdd_expr_num = xdd_expr.subs(rplmts+params_values)
phidd_expr_num = XXX


# preparation done; now we can create the python functions

# generation of the Python functions using sp.lambdify
xdd_fnc = sp.lambdify([x, phi, xd, phid, F], xdd_expr_num, modules="numpy")
phidd_fnc = sp.lambdify(XXX)



## xdd_fnc and phi_dd_fnc are callable objects
## They are functions that expect five arguments each and return a scalar value.




# the code below does not need to be changed




def preview(expr, **kwargs):
     """
     Auxiliary function for "nice" display of extensive expressions (in LaTeX)
     """

     import matplotlib.pyplot as plt
     latex_str = "$ %s $" % sp.latex(expr, **kwargs)
     latex_str = latex_str.replace("operatorname","mathrm")
     plt.figure(figsize=(12, 5))  # 12x5 Zoll
     plt.text(0.5, 0.5, latex_str, fontsize=30, horizontalalignment="center")
     plt.axis("off")
     plt.show()



if __name__ == "__main__":

    # This block will be executed only if this file is the main script,
    # not if it is imported as a module somewhere else.


    # just display the resulting equations

    ## sp.Eq is the sympy-quation type (with left hand side and right hand side)

    Eq1a  = sp.Eq( xdd, xdd_expr.subs(rplmts))
    Eq2a  = sp.Eq( phidd, phidd_expr.subs(rplmts))


    # provide LaTeX notation for the symbols
    sn_dict = {phi: r"\varphi", phid: r"\dot{\varphi}",
               xdd:r"\ddot{x}", phidd:r"\ddot{\varphi}"}

    preview(Eq1a, symbol_names=sn_dict)
    preview(Eq2a, symbol_names=sn_dict)
