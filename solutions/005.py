"""
Problem 5

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
"""
from shared import util


def run():
    start_time = util.now()
    accumulated_factors, product = {}, 1
    lower, upper = 1, 20

    for x in range(lower, upper + 1):

        if x == 1:
            continue

        for prime in util.primes(maximum_value=x, verbose=False):
            unfactored_portion = x
            count = 0

            while util.is_divisor(prime, unfactored_portion):
                count += 1
                unfactored_portion /= prime

            if count:
                accumulated_factors[prime] = max(count, accumulated_factors.get(prime, 0))

    for prime, power in accumulated_factors.items():
        product *= pow(prime, power)

    answer = product
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
