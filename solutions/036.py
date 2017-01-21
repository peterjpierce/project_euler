"""
Problem 36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""
from shared import util


def run():
    start_time = util.now()
    found = set()
    maximum = 999999

    for i in range(1, maximum + 1):
        decimal, binary = str(i), bin(i)[2:]

        if decimal == decimal[::-1] and binary == binary[::-1]:
            found.add(i)
            print('found %s (%s)' % (decimal, binary))

    answer = sum(found)
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
