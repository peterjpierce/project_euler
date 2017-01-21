"""
Problem 35

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from shared import util


def run():
    start_time = util.now()
    found = set()
    maximum = 999999

    primes = set([p for p in util.primes(maximum, verbose=False)])

    for prime in primes:
        digits, all_prime = str(prime), True

        for i in range(1, len(digits)):
            if int(digits[i:] + digits[:i]) not in primes:
                all_prime = False
                break

        if all_prime:
            found.add(prime)
            print('found %d' % prime)

    answer = len(found)
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
