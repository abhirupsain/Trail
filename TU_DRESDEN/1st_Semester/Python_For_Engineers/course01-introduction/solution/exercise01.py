import sys # benötigt für sys.exit()


# ----------  Task 1  ------------------

print("Hello World")


# ----------  Task 2  ------------------
b1 = 3 > 0 # -> True

print("b1:", b1)
print("type(b1):", type(b1))

# Task 3:
# ----------  Task 3  ------------------

L1 = [ 10, 20, "abc"] # Liste
T1 = ("x", "-1", b1, not b1) # Tupel

# mapping from german cities to rivers on which they are located
D1 = {"Dresden" : "Elbe", "Hamburg" : "Elbe", "Frankfurt" : "Main"} # Dictionary
S1 = "abcdefghijklmnopqrstuvwxyz" # String


# ----------  Task 4  ------------------
from ipydex import IPS
# Normally imports should be at the beginning of a file.
# Exception here for didactic reasons.

# Attention: the following code is not suitable for execution in a Jupyter notebook.


print(
    "The next step is to start the IPython shell. ",
    "To exit: use `exit()` or CTRL+D.\n", sep="\n")
input("(Enter)\n")

IPS() # starts the IPython shell in the current namespace
# all objects created / imported so far are available
# to exit: use `exit()` or CTRL+D.



# ----------  Task 5  ------------------

from ipydex import activate_ips_on_exception
activate_ips_on_exception()
# This function ensures that at the point where an (uncaught) error occurs in the program,
# an interactive shell is started which can help to find the cause of the error.

print("In the following an error is provoked by a division by zero.",
      "This will again start an IPython shell at the respective location.",
      "To exit: use `exit()` or CTRL+D.",
      "After that, the script will exit. Code below will *not* be executed.",
      sep="\n")
input("(Enter)\n")
x = 1
y = 0

# z = x/y # this line must be commented out if the further code is to be executed.



# ----------  Task 6  ------------------

print("len(L1):", len(L1))
for x in L1:
    print(L1)

print("len(T1):", len(T1))
for x in T1:
    print(T1)

print("len(D1):", len(D1))
for my_key, my_value in list(D1.items()):
    print("{}: {}".format(my_key, my_value))

print("len(S1):", len(S1))
for x in S1:
    print(x)

# ----------  Task 7  ------------------

from aux_math import is_number

z1 = input("First number? ")
if not  is_number(z1):
    print("Input error")
    sys.exit()
z1 = float(z1)

if z1 <= -10 or z1 >= 10:
    print("Input error (invalid range)")
    sys.exit()

z2 = input("Second number? ")
if not  is_number(z2):
    print("Input error")
    sys.exit()
z2 = float(z2)

if  not -10 <= z2 <= 10: # alternative Schreibweise
    print("Input error (invalid range)")
    sys.exit()

# ----------  Task 8  ------------------
print("Sum:", z1 + z2, "\nAverage:", (z1 + z2)/2.0)

# ----------  Task 9  ------------------
N = 3
zlist = []

print(f"\nNow calcluate the average of {N} numbers:\n")

for i in range(N):
    while True:
        question = f"Number ({i + 1})? "
        r = input(question)
        if is_number(r):
            if not -10 <= float(r) <= 10:
                print("invalid range")
            else:
                # range is OK -> end while loop
                break
        else:
            print("invalid input")

    zlist.append(float(r))

s = sum(zlist)
print("Sum:", s, "\nAverage:", s * 1.0 / len(zlist))
