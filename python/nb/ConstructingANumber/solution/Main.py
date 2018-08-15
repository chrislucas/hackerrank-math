'''
https://www.hackerrank.com/challenges/constructing-a-number/problem
DONE
'''


# Complete the canConstruct function below.
def canConstruct(a):
    # Return "Yes" or "No" denoting whether you can construct the required number.
    acc = 0
    for num in a:
        while num > 0:
            acc += num % 10
            num //= 10
    return acc % 3 == 0


def test():
    _list = [[9], [40, 50, 90], [1, 4]]
    for i in _list:
        print("YEF" if canConstruct(i) else "NO")


test()

if __name__ == '__main__':
    pass
