"""
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt

from shared import util


def run():
    start_time = util.now()
    given_number = 600851475143
    # given_number = 13195
    unsolved_portion, factors = given_number, {}

    for prime in util.primes(maximum_value=sqrt(unsolved_portion)):
        while util.is_divisor(prime, unsolved_portion):
            factors[prime] = factors.get(prime, 0) + 1
            unsolved_portion /= prime
        if unsolved_portion < prime:
            break

    if unsolved_portion > 1:
        factors[unsolved_portion] = 1

    answer = max(factors.keys())
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
