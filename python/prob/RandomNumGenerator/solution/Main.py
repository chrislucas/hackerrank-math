'''
https://www.hackerrank.com/challenges/random-number-generator/problem
'''


def gdc(a, b):
    if a % b == 0:
        return b
    else:
        return gdc(b, a % b)


# Complete the solve function below.
def solve(a, b, c):
    a, b = max(a, b), min(a, b)

    if a + b <= c:
        return 1, 1
    elif a >= c and b >= c:
        x = c * c // 2
        y = (a*b)
        d = gdc(x, y)
        return x//d, y//d

    elif a <= c and b <= c:
        x = (2 * a * b - ((c - b) * (c - b))) // 2
        y = (a*b)
        d = gdc(x, y)
        return x//d, y//d

    x = 0
    y = 0
    d = gdc(x, y)

    return x//d, y//d


def run():
    n = int(input())
    for i in range(0, n):
        a, b, c = list(map(int, input().split()))
        x, y = solve(a, b, c)
        print("%d/%d" % (x, y))
    return


run()

if __name__ == '__main__':
    pass
