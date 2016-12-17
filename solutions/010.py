"""
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
from datetime import datetime as dtime


def primes(maximum_value, verbose=True):
    """Generate a sequence of prime numbers, using Sieve of Eratosthenes."""
    known_nonprimes = set()
    range_stop = maximum_value + 1

    for cursor in range(2, range_stop):
        if cursor not in known_nonprimes:
            more_nonprimes = range(cursor ** 2, range_stop, cursor)
            known_nonprimes.update(more_nonprimes)

            if verbose:
                print('found prime: %12d' % cursor)

            yield cursor


def run():
    start_time = dtime.now()
    total, count = 0, 0
    maximum = 2000000

    for prime in primes(maximum, verbose=True):
        count += 1
        total += prime

    answer = {'sum': total, 'count': count}
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
