'''
https://www.hackerrank.com/challenges/ncr/
'''

def sum_mod(a, b, m):
    return ((a % m) + (b % m)) % m  # (a+b)%m

def multiply_mod(a, b, m):
    return ((a % m) * (b % m)) % m  # (a*b)%m

def combination(n, r):
    mem = [0] * (r+1)
    mem[0] = 1
    for i in range(1, n+1):
        for j in range(min(i, r), 0, -1):
            mem[j] = sum_mod(mem[j], mem[j-1], 142857)
    return mem[r]

def t(n, r):
    if r > n - r:
        r = n - r
    acc = 1
    for i in range(0, r):
        acc = multiply_mod(acc, n - i, 142857)
        acc //= (i + 1)
    return acc

# Complete the solve function below.
def solve(n, r):
    return combination(n, r)


def run():
    cases = int(input())
    while cases > 0:
        n, r = tuple(map(int, input().split(" ")))
        print(solve(n, r))
        cases -= 1


run()

if __name__ == '__main__':
    pass
