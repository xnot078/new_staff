from functools import partial

def exponent(base, power, bias=0):
    return base ** power + bias

print(exponent(2, 3))

root = partial(exponent, power=1/2, bias=1)
root(4)
