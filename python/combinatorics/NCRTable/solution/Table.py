'''
https://www.hackerrank.com/challenges/ncr-table/problem
DONE
'''

def add_mod(a, b, m):
    return ((a%m) + (b%m)) %m


def make_array(n):
    array = [0] * (n+1)
    array[0] = 1
    k = n // 2 + 1
    for i in range(1, n+1):
        for j in range(min(i, k), 0, -1):
            array[j] = add_mod(array[j], array[j-1], 1000000000)

    for i in range(n, k, -1):
        array[i] = array[n-i]

    return array

def test(n):
    k = n // 2 + 1
    acc = 1
    for i in range(0, k):
        acc *= (n-i)
        acc //= (i+1)
        fmt = "%d" if i == 0 else " %d"
        print(fmt % acc, end='')
    print("")
    return


# Complete the solve function below.
def solve(n):
    while n > 0:
        p = int(input())
        array = make_array(p)
        for i in range(0, len(array)):
            fmt = "%d" if i == 0 else " %d"
            print(fmt % array[i], end='')
        print("")
        n -= 1

test(5)

if __name__ == '__main__':
    pass