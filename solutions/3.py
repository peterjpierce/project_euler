"""
Challenge:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt

GIVEN_NUMBER = 600851475143
# GIVEN_NUMBER = 13195


def is_factor(divisor, number):
    """Determine if a number is a factor of another."""
    dividend = number / divisor
    return dividend == int(dividend)

        
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
    largest_prime_factor = 0
    candidate_primes = PrimeGenerator(sqrt(GIVEN_NUMBER))

    for prime in candidate_primes:
        if is_factor(prime, GIVEN_NUMBER):
            largest_prime_factor = prime

    print('answer is: %d' % largest_prime_factor)


if __name__ == '__main__':
    run()
