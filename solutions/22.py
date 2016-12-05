"""
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import csv
from datetime import datetime as dtime
from os.path import abspath, dirname, join

WEIGHTS = {l: i + 1 for i, l in enumerate(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))}


def word_score(word):
    """Decompose and score a word."""
    return sum([WEIGHTS[ltr] for ltr in list(word)])


def run():
    start_time = dtime.now()
    names_file = abspath(join(dirname(__file__), '..', 'input', 'p022_names.txt'))
    total_score, names = 0, []

    with open(names_file, 'r') as f:
        for line in csv.reader(f):
            names.extend(line)

    for idx, name in enumerate(sorted(names)):
        total_score += (idx + 1) * word_score(name)

    answer = total_score
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
