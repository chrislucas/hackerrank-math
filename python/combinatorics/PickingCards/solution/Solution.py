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
        flag = True
        for i in range(0, total):
            if counter_cards[i] < total:
                _map[counter_cards[i]] += 1
            else:
                flag = False
                break

        acc = 0
        if flag:
            acc = 1
            for v in counter_cards:
                q_cards = _map[v]
                acc = mult_mod(acc, q_cards, 1000000007)


        print(acc)


if __name__ == '__main__':
    run()
