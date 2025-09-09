import math

a = 0
b = math.pi / 2
s = 10**(-7)
eps = 10**(-6)
i = 0

while abs((b - a)) > eps:
    i = i + 1
    x1 = (a + b - s) / 2
    x2 = (a + b + s) / 2
    func1 = x1*x1 - math.sin(x1)
    func2 = x2*x2 - math.sin(x2)
    if func1 > func2:
        a = x1
    else:
        b = x2
result = (a + b) / 2
print("результат ", result)
print("итерации ", i)