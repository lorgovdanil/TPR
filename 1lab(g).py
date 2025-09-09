import math

def func(x):
    return x * x - math.sin(x)


a = 0
b = math.pi / 2
s = 10 ** (-7)
eps = 10 ** (-6)
i = 0

x2 = b / ((1 + 5 ** (1 / 2)) / 2)
x1 = b - x2
func1 = func(x1)
func2 = func(x2)
while abs((b - a)) > eps:
    i = i + 1
    if func1 > func2:
        a = x1
        x1 = x2
        x2 = b - x1 + a
        func1 = func2
        func2 = func(x2)
    else:
        b = x2
        x2 = x1
        x1 = b - x2 + a
        func2 = func1
        func1 = func(x1)
resultx = (a + b) / 2
resulty = func(resultx)
print("x", resultx)
print("y", resulty)
print("итерации ", i)
