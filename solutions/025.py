"""
Problem 25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1. Hence, the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
from datetime import datetime as dtime

from shared import util


def run():
    start_time = dtime.now()
    answer, count = None, 0
    # minimum_length = 3
    minimum_length = 1000

    for fibo in util.fibonacci_sequence():
        count += 1
        digits = str(fibo)

        if len(digits) >= minimum_length:
            break

    answer = count
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
