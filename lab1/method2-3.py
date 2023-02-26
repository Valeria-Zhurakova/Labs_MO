# Метод 3
import math

a = -2
b = 0
eps = 0.0001

x_m = (a + b) / 2
f_m = x_m * math.exp(x_m)
l = b - a
k = 0

while True:
    p4 = True
    k = k + 1
    x1 = a + l / 4
    x2 = b - l / 4
    f1 = x1 * math.exp(x1)
    f2 = x2 * math.exp(x2)
    if f1 < f_m:
        b = x_m
        x_m = x1
        p4 = False
    elif p4:
        if f2 < f_m:
            a = x_m
            x_m = x2
        else:
            a = x1
            b = x2
    l = b - a
    if l <= eps:
        break


print("Метод деления отрезка пополам")
if f1 < f_m and f1 < f2:
    print(x1, round(f1, 4))
elif f_m < f1 and f_m < f2:
    print(x_m, round(f_m, 4))
else:
    print(x2, round(f2, 4))

print(k)
print(2 * k + 1)
