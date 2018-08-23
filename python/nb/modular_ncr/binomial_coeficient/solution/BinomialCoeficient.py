'''
https://www.geeksforgeeks.org/binomial-coefficient-dp-9/

C(n, k)
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

https://pt.wikipedia.org/wiki/Bin%C3%B3mio_de_Newton


Coeficiente C(n, k) eh o coeficiente da expansao (x+y)^k

(x+y)^k = somatorio de k=0 ate n C(n, k) x^(n-k)y^k
(x+y)^2 = x^2+2xy+y^2
(x+y)^3 = x^3+3x^2y+3xy^2+y^3
'''


def top_down_solution(n, k):
    if k == 0 or n == k:
        return 1
    else:
        a = top_down_solution(n - 1, k - 1)
        b = top_down_solution(n - 1, k)
        return a + b


def top_down_memoization(n, k, mem):
    if k == 0 or n == k:
        return 1
    elif mem[n][k] > 0:
        return mem[n][k]
    a = top_down_memoization(n - 1, k - 1, mem)
    b = top_down_memoization(n - 1, k, mem)
    mem[n][k] = a + b
    return mem[n][k]


def bottom_up_solution(n, k):
    memo = [[0] * (k + 1) for i in range(0, n + 1)]
    for i in range(0, n + 1):
        for j in range(0, min(i, k) + 1):
            memo[i][j] = 1 if j == 0 or j == i else memo[i - 1][j - 1] + memo[i - 1][j]
    return memo[n][k]


def bottom_up_solution_min_space(n, k):
    memo = [0] * (k + 1)
    memo[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            memo[j] += memo[j - 1]
    return memo[k]


n, k = 100, 2
print(top_down_solution(n, k))
print(top_down_memoization(n, k, [[0] * (k + 1) for i in range(0, n + 1)]))
print(bottom_up_solution(n, k))
print(bottom_up_solution_min_space(n, k))

if __name__ == '__main__':
    pass
