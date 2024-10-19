result_cache = dict()

def cached(func):

    def wrapper(arg):
        key = (func, arg)
        if key in result_cache:
            print("use cached result")
            return result_cache[key]
        else:
            res = func(arg)
            result_cache[key] = res
            return res
    return wrapper

def func1(x):
    print("Executing func1 with x =", x)
    return x**2

wrapped_func1 = cached(func1)

# original function gets called
print(wrapped_func1(5))

# value from the cache gets used
print(wrapped_func1(5))

@cached
def func2(x):
    print("Executing func2 with x =", x)
    return 100 + x

print(func2(4))  # original function gets called
print(func2(4))  # value from the cache gets used
