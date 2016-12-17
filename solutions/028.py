"""
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction
a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
from shared import util


def next_four_corners(last_value, length_of_side):
    """Return values for the next four corners."""
    offset = length_of_side - 1
    return [last_value + (offset * s) for s in (1, 2, 3, 4)]


def run():
    """Visualize the spiral being unwrapped and laid out flat."""
    start_time = util.now()
    center_value = 1
    values = [center_value]
    grid_size = 1001

    for side_length in range(3, grid_size + 1, 2):
        values.extend(next_four_corners(values[-1], side_length))

    answer = sum(values)
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
