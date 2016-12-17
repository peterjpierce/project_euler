"""
Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""
from datetime import datetime as dtime


def run():
    start_time = dtime.now()
    number = 2 ** 1000

    sum_of_digits = sum([int(d) for d in list(str(number))])

    answer = sum_of_digits
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
