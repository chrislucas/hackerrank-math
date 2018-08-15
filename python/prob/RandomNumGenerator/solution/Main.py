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
    total = a + b
    return 0


def run():
    n = int(input())
    for i in range(0, n):
        a, b, c = list(map(int, input().split()))
        print(solve(a, b, c))
    return


run()

if __name__ == '__main__':
    pass
