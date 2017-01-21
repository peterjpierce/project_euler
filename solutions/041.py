"""
Problem 41

We shall say that an n-digit number is pandigital if it makes use of
all the digits 1 to n exactly once. For example, 2143 is a 4-digit
pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
import re

from shared import util

ALL_NINE = '123456789'


def is_pandigital(number):
    """Determine if a integer is pandigital."""
    digits = ''.join(sorted(str(number)))
    unique = set(digits)
    return bool(len(digits) == len(unique) and re.match(digits, ALL_NINE))


def run():
    start_time = util.now()
    answer = None

    for prime in util.primes(10 ** 7, verbose=False):
        if is_pandigital(prime):
            answer = prime
            print('found %d' % prime)

    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
