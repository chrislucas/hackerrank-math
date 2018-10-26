'''
https://www.hackerrank.com/challenges/picking-cards/problem
'''


def mult_mod(a, b, m):
    return ((a % m) * (b % m)) % m


def run():
    cases = int(input().rstrip())
    for k in range(cases):
        total = int(input().rstrip())
        counter_cards = [int(x) for x in input().rstrip().split(" ")]
        _map = [0] * total
        _acc = [0] * total
        flag = True
        for i in range(0, total):
            if counter_cards[i] < total:
                _map[counter_cards[i]] += 1
            else:
                flag = False
                break

        _acc[0] = _map[0]
        for i in range(1, len(_map)):
            _acc[i] = _acc[i-1] + _map[i]

        acc = 0
        if flag:
            acc = 1
            for i in range(0, total):
                val = _acc[i] - i
                if val <= 0:
                    acc = 1
                    break
                acc = mult_mod(acc, val, 1000000007)

        print(acc)


if __name__ == '__main__':
    run()
