'''
https://www.hackerrank.com/challenges/eulers-criterion/problem
https://en.wikipedia.org/wiki/Euler%27s_criterion
'''


def v1(b, e):
    copy_b = 1
    while e > 1:
        if (e & 1) == 0:
            b *= b
            e >>= 1
        else:
            copy_b *= b
            b *= b
            e = (e - 1) >> 1

    return copy_b * b


def v2(b, e):
    c = 1
    while e > 0:
        if (e & 1) == 1:
            c *= b
        b *= b
        e >>= 1
    return c


def exp_it(b, e):
    if e < 0:
        b = 1 / b
        e = -e
    elif e == 0:
        return 1
    elif e == 1:
        return b
    return v2(b, e)


def exp_rec(b, e):
    if e < 0:
        return exp_rec(1 / b, -e)
    elif e == 0:
        return 1
    elif e == 1:
        return b
    elif e & 1 == 0:
        return exp_rec(b * b, e >> 1)
    else:
        return b * exp_rec(b * b, (e - 1) >> 1)


def naive_solution(a, m):
    f = False
    for i in range(2, m):
        if (i * i) % m == a % m:
            f = True
            break
    return "YES" if f else "NO"


def mult_mod(a, b, m):
    return ((a % m) * (b % m)) % m


# teste se a ^(p-1)/2 mod e == 1
def euler_criterion(a, p):
    if a == 0:
        return "YES"
    c = 1
    e = (p-1)//2
    a %= p
    #t = pow(a, e, p)
    while e > 0:
        if (e & 1) == 1:
            c = mult_mod(c, a, p)
        a = mult_mod(a, a, p)
        e >>= 1
    return "YES" if c == 1 else "NO"


# Complete the solve function below.
def solve(a, m):
    return euler_criterion(a, m)


def test():
    for i in [[5, 7], [4, 7]]:
        print(solve(i[0], i[1]))


def test_2():
    n = int(input())
    while n > 0:
        a, m = tuple(map(int, input().split()))
        print(solve(a, m), file=open("..//raw//output.txt", "a"))
        n -= 1

test_2()

if __name__ == '__main__':
    pass
