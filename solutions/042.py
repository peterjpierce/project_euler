"""
Problem 42

The nth term of the sequence of triangle numbers is given by,
tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text
file containing nearly two-thousand common English words, how many are
triangle words?
"""
import csv
from os.path import abspath, dirname, join

from shared import util

WEIGHTS = {l: i + 1 for i, l in enumerate(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))}


def triangle_number(nth):
    """Calculate the value for the nth term."""
    return (nth * (nth + 1)) / 2


def run():
    start_time = util.now()
    words_file = abspath(join(dirname(__file__), '..', 'input', 'p042_words.txt'))
    matches, words = set(), []

    triangle_numbers = [triangle_number(i) for i in range(1, 100)]

    with open(words_file, 'r') as f:
        for line in csv.reader(f):
            words.extend(line)

    for word in words:
        value = 0
        for letter in word:
            value += WEIGHTS[letter]

        if value in triangle_numbers:
            matches.add(word)
            print('found triangle word: %s' % word)

    answer = len(matches)
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (util.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
