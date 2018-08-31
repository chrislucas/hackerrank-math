'''
https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem
DONE
'''


def process(_list_points):
    sum_x, sum_y, sum_xx, sum_xy = 0, 0, 0, 0
    for p in _list_points:
        sum_xx += p[0] * p[0]  # x ^ 2
        sum_xy += p[0] * p[1]  # x * y
        sum_x += p[0]
        sum_y += p[1]

    n = len(_list_points)
    # coeficiente angular
    m = ((n * sum_xy) - (sum_x * sum_y)) / ((n * sum_xx) - (sum_x * sum_x))
    # equacao da reta = y = mx + b
    # m = coeficiente angular, b = coeficiente linear, onde a linha cruza o eixo das ordenadas
    b = (sum_y - (m * sum_x)) / n

    print("Equacao reduzida da reta y = %.3fx + %.3f" % (m, b))
    accError = 0
    for p in _list_points:
        y = m * p[0] + b
        accError += (p[1] - y) * (p[1] - y)
        print("Equacao reduzida da reta y = %fx + %f => %f = %f + %f error %f"
              % (m, b, y, p[0], b, p[1] - y))

    print("Sum of error %f.\n" % accError)
'''
https://pt.wikipedia.org/wiki/M%C3%A9todo_dos_m%C3%ADnimos_quadrados
yi = a + bxi + errori
'''


def lms(values):
    mx, my, n = 0, 0, len(values)
    for v in values:
        mx += v[0] * (1 / n)
        my += v[1] * (1 / n)
    sum_a, sum_b = 0, 0

    residual_square_sum, total_square_sum = 0, 0
    for v in values:
        sum_a += (v[0] - mx) * (v[1] - my)
        sum_b += (v[0] - mx) * (v[0] - mx)
        total_square_sum += (v[1] - my) * (v[1] - my)

    b = sum_a / sum_b
    a = my - b * mx

    '''
        https://www.hackerearth.com/practice/machine-learning/linear-regression/univariate-linear-regression/tutorial/
        https://en.wikipedia.org/wiki/Residual_sum_of_squares
    '''
    for v in values:
        # rss residual sum of square
        rss =  v[1] - (a + b * v[0])
        residual_square_sum += rss * rss

    # https://en.wikipedia.org/wiki/Explained_sum_of_squares
    print("Residual Squarem Sum %f\nTotal Square Sum %f\nExplained square Sum: %f" %
          (residual_square_sum, residual_square_sum, 1 - (residual_square_sum / total_square_sum)))

    for v in values:
        e = v[1] - a + b * v[0]
        print("P(%f, %f) A: %f B: %f Error: %f %f" % (v[0], v[1], a, b, e, 1 - e))

    print("")
    return


matrix = [
    [[2, 4], [3, 5], [5, 7], [7, 10], [9, 15]]
    , [[0, 10], [12, 100], [14, 200], [18, 300], [20, 400], [22, 500], [24, 500], [26, 600]]
    , [[1, 2], [2, 1], [3, 4], [4, 3], [5, 5]]
    , [
        [139, 122], [126, 114], [90, 86], [144, 134]
        , [163, 146], [136, 107], [61, 68], [62, 117], [41, 71], [120, 98]
    ]
    , [
        [60, 3.1], [61, 3.6], [62, 3.8], [63, 4], [65, 4.1]
    ]
]

lms(matrix[4])
process(matrix[4])

if __name__ == '__main__':
    pass
