"""
Problem 4

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from collections import namedtuple

from shared import util

Palindrome = namedtuple('Palindrome', 'value upper lower')


def is_palindrome(number):
    """Determine if a number is a palindrome."""
    got = str(number)
    return bool(got == got[::-1])


def run():
    start_time = util.now()
    verbose = True
    ceiling, floor, biggest, cache = 999, 100, 1, []

    for a in range(ceiling, floor - 1, -1):
        inner_floor = max(int(biggest / a), floor)

        if a * (a - 1) < biggest:
            break

        for b in range(a - 1, inner_floor, -1):
            product = a * b

            if is_palindrome(product):
                found = Palindrome(product, a, b)
                cache.append(found)
                biggest = product if product > biggest else biggest

                if verbose:
                    print('found %s' % str(found))

                break

    answer = biggest
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
