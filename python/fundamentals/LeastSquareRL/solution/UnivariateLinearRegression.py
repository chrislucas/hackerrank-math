'''
https://www.hackerearth.com/practice/machine-learning/linear-regression/univariate-linear-regression/tutorial/
DONE
'''


def ULR(values):
    mean_x, mean_y = 0, 0
    n = len(values)
    for v in values:
        mean_x += v[0] * (1 / n)
        mean_y += v[1] * (1 / n)
    sum_a, sum_b = 0, 0
    for v in values:
        sum_a += (v[1] - mean_y) * (v[0] - mean_x)
        sum_b += (v[0] - mean_x) * (v[0] - mean_x)

    b = sum_a / sum_b
    a = mean_y - b * mean_x

    return a, b


def run():
    q_values = int(input())
    data = [0] * q_values
    for i in range(0, q_values):
        x, y = tuple(map(float, input().split(" ")))
        data[i] = [x, y]
    print("%.6f %.6f" % (ULR(data)))


run()

if __name__ == '__main__':
    pass
