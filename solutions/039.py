"""
Problem 39

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

"""
from shared import util


def run():
    start_time = util.now()
    best = set()
    max_perimeter = 1000

    for perimeter in range(4, max_perimeter):
        tried, found = set(), []

        for a in range(1, int(perimeter / 2)):
            tried.add(a)

            for b in range(int((perimeter - a) / 2), a, -1):
                if b in tried:
                    break
                c = perimeter - (a + b)

                if pow(a, 2) + pow(b, 2) == pow(c, 2):
                    found.append([a, b, c, perimeter])

        if len(found) > len(best):
            best = found.copy()
            print('found new best of length %d' % len(best))

    answer = best
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
