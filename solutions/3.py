"""
Challenge:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
from datetime import datetime as dtime
from math import sqrt


GIVEN_NUMBER = 600851475143
# GIVEN_NUMBER = 13195
# GIVEN_NUMBER = 4097


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
    unsolved_portion, factors = GIVEN_NUMBER, {}
    primes = PrimeGenerator(sqrt(unsolved_portion))

    for prime in primes:
        while is_factor(prime, unsolved_portion):
            factors[prime] = factors.get(prime, 0) + 1
            unsolved_portion /= prime
        if unsolved_portion < prime:
            break

    if unsolved_portion > 1:
        factors[unsolved_portion] = 1

    answer = max(factors.keys())
    print('answer is: %d' % answer)
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
