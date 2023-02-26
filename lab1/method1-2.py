# Метод 2
import math

a = -2
b = 0
eps = 0.0001

h = (b - a) / 4
x_start = a
f0 = x_start * math.exp(x_start)
k = 1

while 1:
    k = k + 1
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

print("Метод поразрядного поиска")
print(x_start, round(f0, 4))

print(k - 1)
print(k)