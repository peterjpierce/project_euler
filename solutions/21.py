"""
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b
 then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.1L

Evaluate the sum of all the amicable numbers under 10000.
"""
from datetime import datetime as dtime

from shared import util


class Number:
    """A number and its divisors."""
    def __init__(self, value):
        self.value = value
        self.divisors = util.proper_divisors(value)

    @property
    def sum_of_divisors(self):
        return sum(self.divisors)

    def __repr__(self):
        return '<Number: %d>' % self.value


def run():
    start_time = dtime.now()
    amicables = set()
    # maximum = 500
    maximum = 9999

    all_numbers = {i: Number(i) for i in range(2, maximum + 1)}

    for number in all_numbers.values():
        try:
            other = all_numbers[number.sum_of_divisors]
            if other.sum_of_divisors == number.value and number != other:
                amicables.update([number.value, other.value])
        except KeyError:
            continue

    answer = sum(amicables)
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
