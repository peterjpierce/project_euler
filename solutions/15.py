"""
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
    (image snipped)
How many such routes are there through a 20×20 grid?

My note:  This is a "40 choose 20" combination calculation, per review of lattice path resources.
"""
from datetime import datetime as dtime


def factorial(number):
    """Calculate factorials."""
    product = 1
    for term in range(number, 1, -1):
        product *= term
    return product


def combinations(set_size, choose_count):
    """Find the value of 'n choose k'."""
    return factorial(set_size) / (factorial(choose_count) * factorial(set_size - choose_count))


def run():
    start_time = dtime.now()
    # grid_size = 2
    grid_size = 20

    number_of_paths = combinations(2 * grid_size, grid_size)

    answer = number_of_paths
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
