"""
Problem 30

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
"""
from shared import util


def run():
    """Visualize the spiral being unwrapped and laid out flat."""
    start_time = util.now()
    values = []
    verbose = True
    power = 5

    powers = {str(i): pow(i, power) for i in range(10)}
    upper_bound = pow(9, power) * (power + 2)

    def sum_power_of_digits(value):
        """Sum each digit of an integer raised to the power."""
        return sum([powers[d] for d in str(int(value))])

    for i in range(2, upper_bound):
        if i == sum_power_of_digits(i):
            values.append(i)
            if verbose:
                print('found %d' % i)

    answer = {'count': len(values), 'sum': sum(values)}
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
