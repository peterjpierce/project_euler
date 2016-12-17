"""
Problem 18

By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

    3
    7 4
    2 4 6
    8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

    (see TRIANGLE below)

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires
a clever method! ;o)ggg
"""
from datetime import datetime as dtime

TRIANGLE = """
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


class Node:
    """Nodes of the triangle, with values and helpers."""
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value
        self.best_next_node = None
        self.best_path = [self]
        self.accumulated_value = value

    def add_best(self, node):
        self.best_next_node = node
        self.best_path += node.best_path
        self.accumulated_value += node.accumulated_value

    def __repr__(self):
        return '<Node: (%d, %d) %d -> %d>' % (
            self.row, self.column, self.value, self.accumulated_value
        )


def run():
    start_time = dtime.now()
    node = None

    # load
    nodes, r = [], 0
    for row in TRIANGLE.split('\n'):
        if row:
            nodes.append([Node(r, c, int(v)) for c, v in enumerate(row.strip().split())])
            r += 1

    # work up from next-to-last row
    for row in range(len(nodes) - 2, -1, -1):
        for col in range(len(nodes[row])):
            node = nodes[row][col]
            a, b = nodes[row + 1][col], nodes[row + 1][col + 1]
            best = a if a.accumulated_value > b.accumulated_value else b
            node.add_best(best)

    answer = node
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
