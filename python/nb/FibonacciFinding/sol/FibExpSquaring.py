'''

'''


def sum_mod(a, b, mod):
    return ((a % mod) + (b % mod)) % mod


def mult_mod(a, b, mod):
    return ((a % mod) * (b % mod)) % mod


def matrix_mult(mat_a, mat_b, mod):
    lin = len(mat_a)
    col = len(mat_b[0])
    mat_c = [[0] * col for i in range(lin)]
    for i in range(0, lin):
        for j in range(0, col):
            for k in range(0, lin):
                mat_c[i][j] = sum_mod(mat_c[i][j], mult_mod(mat_a[i][k], mat_b[k][j], mod), mod)
    return mat_c


def run(n):
    mat = [[0, 1], [1, 1]]
    cpy = [[1, 0], [0, 1]]  # mat
    if n < 2:
        return mat[0][n]

    M = int(10E8 + 7)
    while n > 0:
        if n & 1 == 1:
            cpy = matrix_mult(cpy, mat, M)
        mat = matrix_mult(mat, mat, M)
        n >>= 1
    return cpy[0][0]


def run_test_1():
    for i in range(0, 100):
        print("%d: %d" % (i, run(i)))


def run_test_2(n):
    mat = [[0, 1], [1, 1]]
    state = [[0, 1]]
    M = int(10E8 + 7)
    while n > 1:
        if n & 1 == 1:
            state = matrix_mult(state, mat, M)
        mat = matrix_mult(mat, mat, M)
        n >>= 1
    print(state)



run_test_2(10)

if __name__ == '__main__':
    pass
