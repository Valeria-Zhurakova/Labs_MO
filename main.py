# Метод 2
import math

a = -2
b = 0
eps = 0.0001

h = (b - a) / 4
x_start = a
f0 = x_start * math.exp(x_start)
n = 1

while 1:
    n = n + 1
    p5 = True
    x_res = x_start + h
    f1 = x_res * math.exp(x_res)
    if f0 > f1:
        x_start = x_res
        f0 = f1
        if a < x_start < b:
            p5 = False
    elif p5:
        if abs(h) <= eps:
            break
        else:
            x_start = x_res
            f0 = f1
            h = - h / 4

print(n - 1)
print(n)
print(x_start)
print(round(f0, 4))
