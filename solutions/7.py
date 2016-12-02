"""
Challenge (problem 7)
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
from datetime import datetime as dtime


def is_factor(divisor, number):
    """Determine if a number is a factor of another."""
    return not number % divisor


class PrimeGenerator:
    """Generate a sequence of prime numbers, up to a maximum value."""
    def __init__(self, maximum_value, verbose=True):
        self.maximum = maximum_value
        self.verbose = verbose
        self.found = []

    def __iter__(self):
        self._cursor = 2
        return self

    def __next__(self):
        while self._cursor <= self.maximum:
            is_prime = True

            for prime in self.found:
                if is_factor(prime, self._cursor):
                    is_prime = False
                    break

            if is_prime:
                self.found.append(self._cursor)
                if self.verbose:
                    print('found prime: %12d' % self._cursor)
                return self._cursor

            self._cursor += 1
        raise StopIteration


def run():
    start_time = dtime.now()
    found, count = 0, 0
    look_for = 10001

    primes = PrimeGenerator(pow(10, 20), verbose=True)

    for prime in primes:
        count += 1

        if count == look_for:
            found = prime
            break

    answer = found
    print('answer is: %d' % answer)
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
