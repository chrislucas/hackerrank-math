'''
https://www.hackerrank.com/challenges/fibonacci-finding-easy/problem
https://www.hackerearth.com/practice/notes/matrix-exponentiation-1/
'''


def sum_mod(a, b, mod):
    return ((a % mod) + (b % mod)) % mod


def mult_mod(a, b, mod):
    return ((a % mod) * (b % mod)) % mod


def test_naive(a, b, n):
    if n == 0:
        return a
    elif n == 1:
        return b
    M = int(10E9 + 7)
    acc = sum_mod(a, b, M)
    for i in range(2, n):
        aux = sum_mod(acc, b, M)
        b = acc
        acc = aux
    return acc


def matrix_mult(mat_a, mat_b, mod):
    lin = len(mat_a)
    col = len(mat_b[0])
    mat_c = [[0] * col for i in range(lin)]
    for i in range(0, lin):
        for j in range(0, col):
            for k in range(0, lin):
                mat_c[i][j] = sum_mod(mat_c[i][j], mult_mod(mat_a[i][k], mat_b[k][j], mod), mod)
    return mat_c


def matrix_exp(a, b, n):
    mat = [[0, 1], [1, 1]]
    if n == 0:
        return a
    elif n == 1:
        return b
    M = int(10E8 + 7)
    cpy = [[1, 0], [0, 1]]
    i = n
    while i > 0:
        if i & 1 == 1:
            cpy = matrix_mult(cpy, mat, M)
        mat = matrix_mult(mat, mat, M)
        i >>= 1
    state = [a, b]
    result = [0] * 2
    for i in range(0, 2):
        for j in range(0, 2):
            result[i] = sum_mod(result[i], mult_mod(state[j], cpy[i][j], M), M)
    return result[0]


# Complete the solve function below.
def solve(a, b, n):
    return matrix_exp(a, b, n)


def test():
    _list = [(509618737, 460201239, 229176339)
             ,(920881302, 970435252, 891913774)
        , (2, 3, 1), (0, 1, 7), (9, 1, 7), (9, 8, 3), (2, 4, 9), (4, 3, 1), (3, 7, 5)]
    for i in _list:
        a, b, c = i
        print(solve(a, b, c))


test()

if __name__ == '__main__':
    pass
