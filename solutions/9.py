"""
Problem 8
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which: a2 + b2 = c2
    For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from datetime import datetime as dtime


def run():
    start_time = dtime.now()
    found = []
    perimeter = 1000

    max_side = int(perimeter / 2)

    for side_a in range(1, max_side + 1):
        for side_b in range(max_side, 0, -1):
            side_c = perimeter - side_a - side_b

            if not side_a < side_b < side_c:
                continue
            elif pow(side_a, 2) + pow(side_b, 2) == pow(side_c, 2):
                found.append({
                    'a': side_a, 'b': side_b, 'c': side_c, 'product': side_a * side_b * side_c
                })

    answer = found
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
