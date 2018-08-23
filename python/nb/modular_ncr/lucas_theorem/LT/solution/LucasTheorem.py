'''
https://www.geeksforgeeks.org/compute-ncr-p-set-2-lucas-theorem/
https://brilliant.org/wiki/lucas-theorem/
https://pt.wikipedia.org/wiki/Teorema_de_Lucas
https://www.ime.usp.br/~yw/lic-mat-not-2005/mac110/eps/ep1.pdf
'''


def modular_sum(a, b, m):
    return ((a % m) + (b % m)) % m


def modular_mult(a, b, m):
    return ((a % m) * (b % m)) % m


def ncr_modp(n, r, p):
    memo = [0] * (r + 1)
    memo[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, r), 0, -1):
            memo[j] = modular_sum(memo[j], memo[j - 1], p)
    return memo[r]


'''

'''


def lucas_theorem(n, r, p):
    if r == 0 or n == r:
        return 1
    ni = n % p
    ri = r % p
    a = lucas_theorem(n // p, r // p, p)
    b = ncr_modp(ni, ri, p)
    c = modular_mult(a, b, p)
    return c


'''
teste se nCr gera um numero par ou impar sem
calcula-lo. A forma de fazer isso consiste em converter
n e r numa representacao binaria comparar
bit a bit (a partir do menos significativo) em pares se existe
ao menos 1 bit em 'r' que eh maior que em n
'''


def ncr_odd(n, k):
    flag = True
    while max(n, k) > 0:
        if (k & 1) > (n & 1):
            return False
        n >>= 1
        k >>= 1
    return flag


def test_1():
    print(ncr_odd(8, 2))
    print(ncr_odd(7, 1))
    print(ncr_odd(7, 2))
    print(ncr_odd(7, 3))
    print(ncr_odd(7, 4))
    print(ncr_odd(23, 13))
    print(ncr_odd(23, 5))
    print(ncr_odd(6, 0))
    print(ncr_odd(6, 1))
    print(ncr_odd(6, 2))
    print(ncr_odd(6, 3))
    print(ncr_odd(6, 4))
    print(ncr_odd(8, 3))


def test_2():
    print(lucas_theorem(1000, 300, 13))
    print(lucas_theorem(1000, 900, 13))
    print(lucas_theorem(5, 2, 1001))
    print(lucas_theorem(5, 2, 6))
    print(lucas_theorem(10, 5, 15))
    print(lucas_theorem(20, 6, 210))
    print(lucas_theorem(13, 11, 21))
    print(lucas_theorem(10, 9, 5))


test_2()

if __name__ == '__main__':
    pass
