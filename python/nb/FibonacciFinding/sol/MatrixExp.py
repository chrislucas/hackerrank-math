'''
https://www.geeksforgeeks.org/matrix-exponentiation/
'''


def sum_mod(a, b, mod):
    return ((a % mod) + (b % mod)) % mod


def mult_mod(a, b, mod):
    return ((a % mod) * (b % mod)) % mod


def matrix_mult(mat_a, mat_b, mod):
    lin = len(mat_a)
    col = len(mat_b[0])
    mat_c = [[0] * lin for i in range(col)]
    for i in range(0, lin):
        for j in range(0, col):
            for k in range(0, lin):
                mat_c[i][j] = sum_mod(mat_c[i][j], mult_mod(mat_a[i][k], mat_b[k][j], mod), mod)
    return mat_c


if __name__ == '__main__':
    pass
