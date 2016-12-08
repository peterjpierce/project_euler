"""
Problem 24

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""
from datetime import datetime as dtime

from shared import util


class Number:
    """A number and helpful attributes."""
    def __init__(self, value, verbose=True):
        self.value = value
        self.divisors = util.proper_divisors(value, verbose=verbose)

    @property
    def is_abundant(self):
        return bool(sum(self.divisors) > self.value)

    def __repr__(self):
        return '<Number: %d>' % self.value


def run():
    start_time = dtime.now()
    abundants, abundant_sums, cannots = [], set(), []
    # minimum, maximum = 12, 300
    minimum, maximum = 12, 28123

    all_numbers = [Number(i) for i in range(minimum, maximum + 1)]
    abundants = [n for n in all_numbers if n.is_abundant]

    for i in range(0, len(abundants)):
        for j in range(i, len(abundants)):
            calculated_sum = abundants[i].value + abundants[j].value
            if calculated_sum <= maximum:
                abundant_sums.add(calculated_sum)

    cannots = [i for i in range(1, maximum + 1) if i not in abundant_sums]

    answer = sum(cannots)
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
