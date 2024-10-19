from sympy import sin, cos, Function
import sympy as sp
import sys



# task 1
params = sp.symbols("m1, m2, l, g")
m1, m2, l, g = params



# task 2
t = sp.Symbol("t")  # create the symbol for the time
xt = Function("x")(t)  # x(t)
phit = Function("phi")(t)  # phi(t)

# task 3 (construct four time derivatives)
xdt = xt.diff(t)
phidt = phit.diff(t)
xddt = xt.diff(t, 2)
phiddt = phit.diff(t, 2)


# task 4

# auxiliary quantities
x2t = xt + l*sin(phit)
y2t = -l*cos(phit)

x2dt =x2t.diff(t)
y2dt =y2t.diff(t)

# task 5
# kinetic energy
T = (m1*xdt**2 + m2*(x2dt**2 + y2dt**2))/2

# potential energy
U = y2t*g*m2

L = T - U  # Lagrange funktion

# perform simplifications of expression L
L = L.expand()
L = sp.trigsimp(L)


# --- Lagrange Equations ---

# task 6

# auxiliary expressions:
L_d_x = L.diff(xt)
L_d_phi = L.diff(phit)

L_d_xd = L.diff(xdt)
L_d_phid = L.diff(phidt)

# task 7
DL_d_xd = L_d_xd.diff(t)
DL_d_phid = L_d_phid.diff(t)


# task 8
F = sp.Symbol("F")  # external force (translatoric)



# right hand side of the equations of motion (left hand side is zero)
Eq1 =  DL_d_xd - L_d_x - F
Eq2 =  DL_d_phid - L_d_phi


# useful for debugging: pretty printing
sp.pprint(Eq1)
sp.pprint(Eq2)


# task 9
# list of accelerations
acc = [xddt, phiddt]

# solve equations for acceleration symbols
res = sp.solve([Eq1, Eq2], acc)

# task 10

msg = f"\nThe variable `res` is of type: {type(res)} and has the following value:\n"
print(msg)
sp.pprint(res)

xdd_expr = res[xddt]
phidd_expr = res[phiddt]


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
params_values = [(m1, 0.8), (m2, 0.3), (l, 0.5), (g, 9.81)]


# perform subsitution and save result in variables
# note: a sum of lists is a new list containing all elements
xdd_expr_num = xdd_expr.subs(rplmts+params_values)
phidd_expr_num = phidd_expr.subs(rplmts+params_values)

# preparation done; now we can create the python functions

# generation of the Python functions using sp.lambdify
xdd_fnc = sp.lambdify([x, phi, xd, phid, F], xdd_expr_num, modules="numpy")
phidd_fnc = sp.lambdify([x, phi, xd, phid, F], phidd_expr_num, modules="numpy")



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
