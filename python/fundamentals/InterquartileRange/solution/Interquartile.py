'''
https://www.hackerrank.com/challenges/s10-interquartile-range/problem

DONE
'''


def is_odd(n):
    return n & 1 == 1


def interquartile_range(Q):
    Q.sort()
    n = len(Q)
    q1, q2, q3, irq = 0, 0, 0, 0
    mid = n // 2
    inf_quarter = n // 4
    sup_quarter = (n - mid) // 2 + mid
    if is_odd(mid):
        q1 = Q[inf_quarter]
        q3 = Q[sup_quarter]
        irq = q3 - q1
    else:
        q1 = (Q[inf_quarter] + Q[inf_quarter - 1]) // 2
        si = sup_quarter - 1 if n & 1 == 0 else sup_quarter + 1
        q3 = (Q[sup_quarter] + Q[si]) // 2
        irq = q3 - q1
    '''
    if is_odd(n):
        q2 = Q[mid]
    else:
        q2 = (Q[mid] + Q[mid - 1]) // 2
    '''
    return "%.1f" % irq #q1, q2, q3, irq


def run():
    n = int(input())
    S = list(map(int, input().split(" ")))
    F = list(map(int, input().split(" ")))
    Q = []

    for i in range(0, n):
        for j in range(0, F[i]):
            Q.append(S[i])

    Q.sort()
    return interquartile_range(Q)


print(run())
'''
print(solution([4, 17, 7, 14, 18, 12, 3, 16, 10, 4, 4, 12]))
print(solution([3, 7, 8, 5, 12, 14, 21, 15, 18, 14]))
print(solution([3, 7, 8, 5, 12, 14, 21, 13, 18]))
'''


if __name__ == '__main__':
    pass
