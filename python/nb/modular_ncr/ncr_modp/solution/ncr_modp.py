def modular_sum(a, b, m):
    return ((a % m) + (b % m)) % m


'''
1           -> (x+y) ^ 0
1 1         -> (x+y) ^ 1
1 2 1       -> (x+y) ^ 2
1 3 3 1
1 4 6 4 1
'''


def ncr_modp(n, r, p):
    memo = [0] * (r + 1)
    memo[0] = 1
    for i in range(1, (n + 1)):
        for j in range(min(i, r), 0, -1):
            memo[j] = modular_sum(memo[j], memo[j - 1], p)
    return memo[r]


print(ncr_modp(5, 2, int(10E6+7)))
print(ncr_modp(10, 2, 13))
print(ncr_modp(10, 2, int(10E9+7)))

if __name__ == '__main__':
    pass
