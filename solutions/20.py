"""
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
from datetime import datetime as dtime


def factorial(number):
    """Calculate factorials."""
    product = 1
    for term in range(number, 1, -1):
        product *= term
    return product


def run():
    start_time = dtime.now()

    answer = sum([int(d) for d in list(str(factorial(100)))])

    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
