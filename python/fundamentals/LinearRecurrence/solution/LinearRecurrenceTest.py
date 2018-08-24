'''

f(i) = f(i-1) + f(i-2)
k = 2

Nao se esquercer dos termos ausentes
f(i) = f(i-2) + f(i-4)
f(i) = 0f(i-1) + f(i-2) + 0f(i-3) + f(i-4)
k = 4
'''


# fn(n) 2fn(n-1) - fn(n-2)
def fn(n):
    if n == 0:
        return 0
    elif n == 1:
        return 3
    else:
        return 2 * fn(n - 1) - fn(n - 2)


def multiplication_mat(a, b):
    _lin = len(a)
    _col = len(b[0])
    mat = [[0] * _col for i in range(0, _lin)]
    for i in range(0, _lin):
        for j in range(0, _col):
            for k in range(0, _lin):
                mat[i][j] += a[i][k] * b[k][j]
    return mat


def fn_matrix(mat, n, f):
    # mat = [[0, 1], [1, 1]]
    # cpy = [[0, 1], [1, 1]] #[[1, 0], [0, 1]]
    cpy = mat
    while n > 0:
        if n & 1 == 1:
            cpy = multiplication_mat(cpy, mat)
        mat = multiplication_mat(mat, mat)
        n >>= 1
    #cpy = multiplication_mat(cpy, f)
    return cpy[0][0]


'''
print(fn(10))
print(fn_matrix([[0, 1], [1, 1]], 9, [[0], [3]]))
'''
'''
print(fn_matrix([[0, 1], [1, 1]], 8, [[1], [1]]))
mat = [
    [2, 2, 2, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]
]
f = [[1], [1], [1], [1]]
print(fn_matrix(mat, 10, f))
'''


# f(n) = c1f(n-1) + c2f(n-2) + c3f(n-3)
# c1, c2, c3 = 0, 1, 1
mat = [
    [1, 1, 1], [1, 0, 0], [0, 1, 0]
]
# f(0) = 0, f(1) = 1, f(2) = 1
f = [[0], [1], [1]]

print(fn_matrix(mat, 5, f))


if __name__ == '__main__':
    pass
