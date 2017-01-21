"""
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial
of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from shared import util


def run():
    start_time = util.now()
    found = []

    for candidate in range(3, 100000):
        if candidate == sum([util.factorial(int(d)) for d in str(candidate)]):
            found.append(candidate)
            print('found %d' % candidate)

    answer = sum(found)

    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
