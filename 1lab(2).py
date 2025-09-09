import math

def func(x):
    return x * x - math.sin(x)


a = 0
b = math.pi / 2
s = 10 ** (-7)
eps = 10 ** (-6)
i = 0

while abs((b - a)) > eps:
    i = i + 1
    x1 = (a + b - s) / 2
    x2 = (a + b + s) / 2
    func1 = func(x1)
    func2 = func(x2)
    if func1 > func2:
        a = x1
    else:
        b = x2
resultx = (a + b) / 2
resulty = func(resultx)
print("x", resultx)
print("y", resulty)
print("итерации", i)
