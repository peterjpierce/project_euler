"""
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from shared import util


def run():
    start_time = util.now()
    found, count = 0, 0
    look_for = 10001

    for prime in util.primes(pow(10, 6), verbose=True):
        count += 1

        if count == look_for:
            found = prime
            break

    answer = found
    print('answer is: %d' % answer)
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
