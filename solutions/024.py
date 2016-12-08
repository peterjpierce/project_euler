"""
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the
digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from datetime import datetime as dtime
from itertools import permutations


def run():
    start_time = dtime.now()
    count, got = 0, None
    want = 1000000

    for word in permutations(list('0123456789')):
        count += 1

        if count == want:
            got = ''.join(word)
            break

    answer = got
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
