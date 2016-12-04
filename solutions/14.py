"""
Problem 14
The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting
numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
from datetime import datetime as dtime


def next_number(number):
    if number % 2:
        return 3 * number + 1
    return number / 2


def run():
    start_time = dtime.now()
    cached_shortcuts = {}
    longest = {'start': None, 'terms_count': 0}
    max_number = 999999
    # max_number = 13

    for number in range(2, max_number + 1):
        cursor, terms_count = number, 1

        while cursor > 1:
            if cursor in cached_shortcuts:
                terms_count += (cached_shortcuts[cursor] - 1)
                break

            cursor = next_number(cursor)
            terms_count += 1

        cached_shortcuts[number] = terms_count

        if terms_count > longest['terms_count']:
            longest.update({'start': number, 'terms_count': terms_count})

    answer = longest
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
