'''
https://www.hackerrank.com/challenges/cheese-and-random-toppings/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
'''


# Complete the solve function below.
def solve(n, r, p):
    if r == 0 or r == n:
        return 1
    pn, pr = n%p, r%p
    a = solve(n//p, r//p, p)
    b = modular_ncr(pn, pr, p)
    return modular_multiplication(a, b, p)


def modular_sum(a, b, m):
    return ((a % m) + (b % m)) % m


def modular_multiplication(a, b, m):
    return ((a % m) * (b % m)) % m


def modular_ncr(n, r, m):
    mem = [0] * (r + 1)
    mem[0] = 1
    for i in range(0, n + 1):
        for j in range(min(i, r), 0, -1):
            mem[j] = modular_sum(mem[j], mem[j - 1], m)
    return mem[r]


def run():
    cases = int(input())
    while cases > 0:
        n, r, m = list(map(int, input().split(" ")))
        print(solve(n, r, m), file=open("..//raw//output.txt", "a"))
        cases -= 1


run()

if __name__ == '__main__':
    pass
