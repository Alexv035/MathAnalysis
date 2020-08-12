'''
Написать на python алгоритм, по вычислению значений sin(x) [0, 30]
Для проверки подойдут данные из таблицы Брадиса
'''

import numpy as np

# n = float(input('input n: '))
n = 30
k = 1.0
t = k
rn = 0

while t <= n:
    r = rn
    if n == 0:
        break
    elif t == 0:
        rn = k * np.pi / 180
    else:
        rn = r + np.sqrt(1 - r ** 2) * k * np.pi / 180

    if t / round(t, 0) == 1.0:
        print(f'x = {round(t, 1)}, sin(x) = {round(rn, 4)}')

    if t == 9.0:
        k = 0.2
    elif t == 18:
        k = 0.2
    elif t == 26:
        k = 0.01

    t = round(t + k, 2)

#print(round(rn, 4))
