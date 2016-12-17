"""
Problem 31

In England the currency is made up of pound, £, and pence, p, and there
are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""
from collections import namedtuple

from shared import util


FACE_VALUES = {'l2': 200, 'l1': 100, 'p50': 50, 'p20': 20, 'p10': 10, 'p5': 5, 'p2': 2, 'p1': 1}

Coins = namedtuple('Coins', 'l2 l1 p50 p20 p10 p5 p2 p1')


def coins_value(coins):
    """Return the total value for a Coins instance."""
    return sum([FACE_VALUES[k] * v for k, v in coins._asdict().items()])


def run():
    """Visualize the spiral being unwrapped and laid out flat."""
    start_time = util.now()
    solutions, zeroes = [], Coins(0, 0, 0, 0, 0, 0, 0, 0)
    verbose = True
    goal = 200

    def range_upper(coins_so_far, denomination):
        """Get range boundary for a denomination given coins already used."""
        return int((goal - coins_value(coins_so_far)) / FACE_VALUES[denomination]) + 1

    for l2 in range(0, range_upper(zeroes, 'l2')):
        coins = zeroes._replace(l2=l2)

        for l1 in range(0, range_upper(coins, 'l1')):
            coins = coins._replace(l1=l1)

            for p50 in range(0, range_upper(coins, 'p50')):
                coins = coins._replace(p50=p50)

                for p20 in range(0, range_upper(coins, 'p20')):
                    coins = coins._replace(p20=p20)

                    for p10 in range(0, range_upper(coins, 'p10')):
                        coins = coins._replace(p10=p10)

                        for p5 in range(0, range_upper(coins, 'p5')):
                            coins = coins._replace(p5=p5)

                            for p2 in range(0, range_upper(coins, 'p2')):
                                coins = coins._replace(p2=p2)

                                for p1 in range(0, range_upper(coins,  'p1')):
                                    coins = coins._replace(p1=p1)

                                    if coins_value(coins) == goal:
                                        solutions.append(coins)

                                        if verbose:
                                            print('found %s' % str(coins))

                                coins = coins._replace(p1=0)
                            coins = coins._replace(p2=0)
                        coins = coins._replace(p5=0)
                    coins = coins._replace(p10=0)
                coins = coins._replace(p20=0)
            coins = coins._replace(p50=0)
        coins = coins._replace(l1=0)

    answer = {'count': len(solutions)}
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
