"""
Challenge (problem 6)
The sum of the squares of the first ten natural numbers is,
    12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
from datetime import datetime as dtime


def run():
    start_time = dtime.now()
    lower, upper = 1, 100

    sum_of_square = sum([pow(i, 2) for i in range(lower, upper + 1)])
    square_of_sum = pow(sum([i for i in range(lower, upper + 1)]), 2)

    answer = square_of_sum - sum_of_square
    print('answer is: %d' % answer)
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
