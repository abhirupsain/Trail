import math 
print("Hello World")
a = 10
b = 20.5
c = a + b + 3**2
print(math.sqrt(c))

while True: # start infinite loop
    x = input("Your name? ")  # returns a str-object
    if x == "q":
        break # finish loop
    print("Hello ", x)
