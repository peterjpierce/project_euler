#!/usr/bin/env python

#  By considering the terms in the Fibonacci sequence whose values do
#  not exceed four million, find the sum of the even-valued terms.

MAX = 4000000


def next_one(current_sequence):
    return sum(current_sequence[-2:])


def run():
    fibonacci = [1, 2]
    next_element = next_one(fibonacci)

    while next_element < MAX:
        fibonacci.append(next_element)
        next_element = next_one(fibonacci)

    answer = sum([f for f in fibonacci if not f % 2])
    print(answer)


if __name__ == '__main__':
    run()
