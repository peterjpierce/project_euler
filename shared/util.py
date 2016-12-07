def factorial(number):
    """Calculate factorials

    Args:
        number (int): the number for which to calculate.

    Returns:
        The (int) factorial.
    """
    product = 1
    for term in range(number, 1, -1):
        product *= term
    return product


def primes(maximum_value, verbose=True):
    """Generate a sequence of prime numbers, using Sieve of Eratosthenes.

    Args:
        maximum_value (int) or (float): the upper limit of primes to generate.
        verbose (bool): prints primes found to stdout if True.

    Returns:
        Yields a sequence of prime numbers, one per iteration.
    """
    known_nonprimes = set()
    range_stop = int(maximum_value) + 1

    for cursor in range(2, range_stop):
        if cursor not in known_nonprimes:
            more_nonprimes = range(cursor ** 2, range_stop, cursor)
            known_nonprimes.update(more_nonprimes)

            if verbose:
                print('found prime: %12d' % cursor)

            yield cursor


def is_divisor(factor, number):
    """Determine if a potential factor divides cleanly.

    Args
        factor (int): potential divisor
        number (int): the bigger number to test against.

    Returns:
        True or False.
    """
    return not bool(number % factor)


def proper_divisors(number):
    """Find proper divisors of a number.

    Args:
        number (int): the number to resolve.

    Returns:
        A list of integers.
        """
    range_stop = int((number / 2) + 1)
    candidates = set(range(1, range_stop))
    found = []

    while len(candidates):
        candidate = candidates.pop()
        if is_divisor(candidate, number):
            found.append(candidate)
        else:
            candidates.difference_update(range(candidate ** 2, range_stop, candidate))

    return found
