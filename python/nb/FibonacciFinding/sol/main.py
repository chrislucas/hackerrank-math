'''
https://www.hackerrank.com/challenges/fibonacci-finding-easy/problem
https://www.hackerearth.com/practice/notes/matrix-exponentiation-1/
'''


def sum_mod(a, b, mod):
    return ((a % mod) + (b % mod)) % mod


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
    mat_c = [[0] * lin for i in range(col)]
    for i in range(0, lin):
        for j in range(0, col):
            for k in range(0, lin):
                mat_c[i][j] = sum_mod(mat_c[i][j], mat_a[i][k] * mat_b[k][j], mod)
    return mat_c


def matrix_exp(a, b, n):
    mat = [[a, b], [b, 1]]
    if n == 0:
        return mat[0][0]
    elif n == 1:
        return mat[0][1]
    M = int(10E9 + 7)
    cpy = [[a, b], [b, 1]]
    i = n
    while i > 0:
        if i & 1 == 1:
            cpy = matrix_mult(cpy, cpy, M)
            i >>= 1
        else:
            mat = matrix_mult(mat, cpy, M)
            i = (i-1) >> 1
    return cpy[1][1]


# Complete the solve function below.
def solve(a, b, n):
    return matrix_exp(a, b, n)


def test():
    _list = [(2, 3, 1), (0, 1, 7), (9, 1, 7), (9, 8, 3), (2, 4, 9), (3, 7, 5)]
    for i in _list:
        a, b, c = i
        print(solve(a, b, c))


test()

if __name__ == '__main__':
    pass
