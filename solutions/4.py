"""
Challenge (problem 4):
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
from collections import namedtuple
from datetime import datetime as dtime

Palindrome = namedtuple('Palindrome', 'value upper lower')


def is_palindrome(number):
    """Determine if a number is a palindrome."""
    got = str(number)
    return bool(got == got[::-1])


def run():
    start_time = dtime.now()
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
    print('answer is: %d' % answer)
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
