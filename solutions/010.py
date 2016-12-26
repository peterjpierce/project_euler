"""
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from shared import util


def run():
    start_time = util.now()
    total, count = 0, 0
    maximum = 2000000

    for prime in util.primes(maximum, verbose=True):
        count += 1
        total += prime

    answer = {'sum': total, 'count': count}
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
