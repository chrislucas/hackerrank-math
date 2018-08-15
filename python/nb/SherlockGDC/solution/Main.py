'''
https://www.hackerrank.com/challenges/sherlock-and-gcd/problem
DONE
'''


def gdc(a, b):
    if a % b == 0:
        return b
    else:
        return gdc(b, a % b)


def test_2(a):
    n = len(a)
    if n == 1:
        return "NO"
    else:
        has_repeated_e = False
        has_problem = False
        for i in range(1, 1 << n):
            subset = []
            has_repeated_e = False
            for j in range(0, n):
                k = 1 if i & (1 << j) > 0 else 0
                if k == 1:
                    if a[j] in subset:
                        has_repeated_e = True
                        break
                    subset.append(a[j])
            if has_repeated_e:
                break
            if len(subset) > 1:
                for i in range(0, len(subset) - 1):
                    if subset[i] == 1:
                        del subset[i]
                gdc_c = 1
                if len(subset) > 1:
                    gdc_c = gdc(subset[0], subset[1])
                    for i in range(2, len(subset)):
                        gdc_c = gdc(gdc_c, subset[i])
                if gdc_c > 1:
                    has_problem = True
                    break
        if has_repeated_e:
            return "NO"
        return "NO" if has_problem else "YES"


def test_3(a):
    if len(a) > 1:
        acc = gdc(a[0], a[1])
        for i in range(2, len(a)):
            acc = gdc(acc, a[i])
        return "YES" if acc == 1 else "NO"
    else:
        return "YES"


# Complete the solve function below.
def solve(a):
    test_3(a)


def test():
    '''
    :return:
        _list = [[1,2,3], [1, 2, 3, 4], [2, 4], [5,5,5]]
        for i in _list:
            solve(i)
    '''
    cases = int(input())
    while cases > 0:
        n = int(input())
        _list = list(map(int, input().split(" ")))
        print(solve(_list))
        cases -= 1


test()

if __name__ == '__main__':
    pass
