#!/usr/bin/env python

#  Challenge:
#  By considering the terms in the Fibonacci sequence whose values do
#  not exceed four million, find the sum of the even-valued terms.

MAX = 4000000


class FiboGenerator:
    """Generate a Fibonacci sequence, up to a maximum value."""
    def __init__(self, maximum_value):
        self.maximum = maximum_value
        self._last_two = [0, 0]

    def __iter__(self):
        return self

    def __next__(self):
        a, b = self._last_two
        next_value = a + b if b > 1 else b + 1

        if next_value > self.maximum:
            raise StopIteration

        self._last_two = [b, next_value]
        return next_value


def run():
    fibo = FiboGenerator(MAX)
    answer = sum([f for f in fibo if not f % 2])
    print(answer)


if __name__ == '__main__':
    run()
