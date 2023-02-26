# Метод 6

import math


def func(x):
    return x * math.exp(x)


a = -2
b = 0
eps = 0.0001
d = eps / 2

fib = [1, 1]
n = 1

while True:
    if fib[n] > (b - a) / eps:
        break
    else:
        fib.append(fib[n] + fib[n - 1])
        n += 1
x1 = a + (fib[n - 2] / fib[n]) * (b - a)
x2 = a + (fib[n - 1] / fib[n]) * (b - a)

f1 = func(x1)
f2 = func(x2)
k = 1

while True:
    flg7 = False
    if f1 > f2:
        a = x1
        x1 = x2
        f1 = f2
        x2 = a + (fib[n - k - 1] / fib[n - k]) * (b - a)
        if k == n - 2:
            flg7 = True
        else:
            f2 = func(x2)
    else:
        b = x2
        x2 = x1
        f2 = f1
        x1 = a + (fib[n - k - 2] / fib[n - k]) * (b - a)
        if k == n - 2:
            flg7 = True
        else:
            f1 = func(x1)
    if flg7:
        x2 = x1 + d
        if func(x1) > func(x2):
            a = x1
        else:
            b = x2
        break
    else:
        k += 1

print("Метод Фибоначчи")
print((a + b) / 2, round(func((a + b) / 2), 4))

print(k)
print(k + 2)
