"""
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""
from shared import util


def candidate(numerator, denominator):
    """Find non-trivial cases to check and return cancelled result."""
    n0, n1, d0, d1 = [int(v) for v in '%02d%02d' % (numerator, denominator)]

    if n1 == d1:
        return None
    elif n1 == d0:
        return n0, d1
    elif n0 == d1:
        return n1, d0
    else:
        return None


def run():
    start_time = util.now()
    curious, products, factors, answer = [], {'n': 1, 'd': 1}, {}, 1
    lower, upper = 11, 99

    for numerator in range(lower, upper + 1):
        for denominator in range(numerator + 1, upper + 1):
            reduced = candidate(numerator, denominator)

            if reduced:
                n, d = reduced

                if n * denominator == numerator * d:
                    found = {'n': numerator, 'd': denominator}
                    curious.append(found)
                    print('found %s' % str(found))

    for t in 'nd':
        for value in [c[t] for c in curious]:
            products[t] *= value
        factors[t] = util.find_factors(products[t])

    least_denominator_factors = factors['d'].copy()
    for factor, power in least_denominator_factors.items():
        if factor in factors['n']:
            power = max(power - factors['n'][factor], 0)
        answer *= pow(factor, power)

    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
