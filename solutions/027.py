"""
Problem 27

Euler discovered the remarkable quadratic formula:

    n^2+n+41

It turns out that the formula will produce 40 primes for the consecutive
integer values 0≤n≤39. However, when n=40, 40^2+40+41 is divisible by 41,
and certainly when n=41,41^2+41+41, 41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes
for the consecutive values 0≤n≤79. The product of the coefficients,
−79 and 1601, is −126479.

Considering quadratics of the form:

    n^2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n, e.g. |11|=11 and |−4|=4

Find the product of the coefficients, aa and bb, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n=0.
"""
from shared import util


class EmptyPrimes(Exception):
    """Warn if the primes set is exhausted."""
    pass


def quadratic_factory(a, b):
    """Provide a quadratic function for the given coefficients."""
    def formula(n):
        return (n ** 2) + (a * n) + b
    return formula


def run():
    start_time = util.now()
    best, verbose = {'count': 0}, False

    primes = set([p for p in util.primes(1000 ** 2, verbose=False)])
    largest_prime = max(primes)

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            quadratic = quadratic_factory(a, b)
            n = 0

            while quadratic(n) in primes:
                n += 1
                if verbose:
                    print('a=%d, b=%d, n=%d' % (a, b, n))

            if quadratic(n) > largest_prime:
                raise EmptyPrimes('ran out on %d (a=%d, b=%d, n=%d)' % (quadratic(n), a, b, n))

            if n > best['count']:
                best = {'count': n, 'a': a, 'b': b, 'ab': a * b, 'biggest_prime': quadratic(n - 1)}

    answer = best
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
