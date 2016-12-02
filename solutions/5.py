"""
Challenge (problem 5)
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
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
    accumulated_factors, product = {}, 1
    lower, upper = 1, 20

    for x in range(lower, upper + 1):

        if x == 1:
            continue

        applicable_primes = PrimeGenerator(maximum_value=x, verbose=False)

        for prime in applicable_primes:
            unfactored_portion = x
            count = 0

            while is_factor(prime, unfactored_portion):
                count += 1
                unfactored_portion /= prime

            if count:
                accumulated_factors[prime] = max(count, accumulated_factors.get(prime, 0))

    for prime, power in accumulated_factors.items():
        product *= pow(prime, power)

    answer = product
    print('answer is: %d' % answer)
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
