"""
Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.
"""
from datetime import datetime as dtime
from decimal import Decimal, getcontext

from shared import util


def repeating_decimal(numerator, divisor, min_length=5):
    """Find the repeating part of a fraction's decimal equivalent.

    Args:
        numerator (int): the top part of the fraction
        divisor (int): the bottom part of the fraction
        min_length (int): disregard results shorter than this

    Returns:
        A (str) of digits, or None.
    """
    getcontext().prec = 10000
    number_string = str(Decimal(numerator) / Decimal(divisor))[:-2]
    size, stop_looking_size, found = min_length - 1, len(number_string) / 2, None

    def trailing_chunks(length):
        """Return last two substrings of the given length."""
        return number_string[-length:], number_string[-2 * length:-length]

    while not (found or size > stop_looking_size):
        size += 1
        a, b = trailing_chunks(size)
        if a == b:
            found = a

    # block smaller repeating patterns
    for subsize in util.proper_divisors(size):
        a, b = trailing_chunks(subsize)
        if a == b:
            return None

    return found if found else None


def run():
    start_time = dtime.now()
    longest = {}
    # denominators = range(1, 12)
    denominators = range(1, 1000)

    for d in denominators:
        candidate = repeating_decimal(1, d)
        if candidate and len(candidate) > longest.get('pattern_length', 0):
            longest = dict(denominator=d, pattern=candidate, pattern_length=len(candidate))

    answer = longest
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
