"""
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying
by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the
concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
from shared import util

ALL_NINE = set('123456789')


def is_nine_pandigital(number):
    """Determine if a integer is 1-to-9 pandigital."""
    digits = str(number)
    return bool(len(digits) == len(ALL_NINE) and set(digits) == ALL_NINE)


def concatenated_product(number, series_max):
    """Calculate the 'concatenated product'."""
    products = [number * i for i in range(1, series_max + 1)]
    return int(''.join([str(p) for p in products])) if products else 0


def run():
    start_time = util.now()
    max_found = {'number': 0, 'series_max': 0, 'product': 0}

    # honestly just brute-forcing these ranges
    for number in range(2, 20000):
        for series_max in range(20, 1, -1):
            product = concatenated_product(number, series_max)

            if product < max_found['product']:
                break
            elif is_nine_pandigital(product):
                max_found = {'number': number, 'series_max': series_max, 'product': product}
                print('found new maximum: %s' % str(max_found))

    answer = max_found
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
