# Note: the id(...) function returns a unique identity-number for each object.
# Same number means: same object.

class ClassA():
  def m1(self):
      print(id(self))

  def m2(x):  # !! self argument missing
      print(x)

a = ClassA()  # create an instance

a.m1()  # no explicit argument (but implicitly a is passed)
print(id(a))  # this gives the same number

a.m2()  # no error (corresponds to print(id(a)), because x takes the role of self)
a.m2(123)  # Error: too many arguments passed (a (implicitly) and 123 (explicitly))
