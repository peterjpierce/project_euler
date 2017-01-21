"""
Problem 40
Champernowne's constant

An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of
the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
from shared import util


def run():
    start_time = util.now()
    digits, answer = '', 1
    max_needed = 1000000

    for i in range(max_needed):
        digits += str(i)
        if len(digits) > max_needed:
            break

    for power in range(7):
        answer *= int(digits[10 ** power])

    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
