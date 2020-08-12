'''
На языке Python предложить алгоритм вычисляющий численно предел
x/((x!)^(1/x))
'''

def PTree(l, r, n):
    if (l > r):
        return 1
    if (l == r):
        return l ** (1 / n)
    if (r - l == 1):
        return (l ** (1 / n)) * (r ** (1 / n))
    m = int((l + r) / 2)
    return PTree(l, m, n) * PTree(m + 1, r, n)


def FTree(n):
    if (n < 0): return 0
    if (n == 0): return 1
    if (n == 1): return n
    if (n == 2): return n ** (1 / n)
    return PTree(2, n, n)


n = 20000
y = FTree(n)
z = (n / y)

#k = n / (2*3*4*5*6*7*8*9*10)**(1/n)
#print(z,k)

n = 200000

while True:
    y = FTree(n)

    try:
        z1 = (n / y)
    except:
        print('error', n)
        break

    if n == 10000000:
        break
    elif z1 - z < 1 / 10 ** 6:
        print(f'Предел с погрешностью 10^(-6) равен: {z1}, достигнут при n = {n}')
        break
    else:
        n += 25000
        z = z1
        #print(z1)

# Предел с погрешностью 10^(-6) равен: 2.718253086428405, достигнут при n = 725000
# Предел с погрешностью 10^(-7) равен: 2.7182789833055643, достигнут при n = 8500000