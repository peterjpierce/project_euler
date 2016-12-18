"""
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""
import itertools

from shared import util


def run():
    start_time = util.now()
    digits = set([str(i) for i in range(1, 10)])
    factors_length = int(len(digits) / 2) + 1
    verbose = True
    solutions = []

    for first_length in range(1, int(factors_length / 2) + 1):
        second_length = factors_length - first_length

        for digits_a in itertools.permutations(digits, first_length):
            factor_a = int(''.join([d for d in digits_a]))

            for digits_b in itertools.permutations(digits - set(digits_a), second_length):
                factor_b = int(''.join([d for d in digits_b]))
                product = factor_a * factor_b
                unique_digits = set([d for d in str(product)])

                if len(unique_digits) != len(str(product)):
                    continue

                if set([d for d in str(product)]) == digits - (set(digits_a) | set(digits_b)):
                    solution = {'a': factor_a, 'b': factor_b, 'product': product}
                    solutions.append(solution)

                    if verbose:
                        print('found %s' % str(solution))

    answer = {
        'count': len(solutions),
        'sum_unique_products': sum(set([s['product'] for s in solutions])),
    }
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
