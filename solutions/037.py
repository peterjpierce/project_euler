"""
Problem 37

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain prime
at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from shared import util


def run():
    start_time = util.now()
    found = set()
    maximum = 999999

    primes = set([p for p in util.primes(maximum, verbose=False)])

    for prime in primes:
        if prime <= 7:
            continue

        digits, valid = str(prime), True

        for i in range(1, len(digits)):
            if not (int(digits[i:]) in primes and int(digits[:-i]) in primes):
                valid = False
                break

        if valid:
            found.add(prime)
            print('found %s' % prime)

    answer = sum(found)
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
