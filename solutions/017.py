"""
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there
are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
from datetime import datetime as dtime

WORDS = {
    'digits': {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
        8: 'eight', 9: 'nine',
    },
    'teens': {
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
        16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    },
    'tens': {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy',
        8: 'eighty', 9: 'ninety',
    },
}


def number_phrase(number):
    """Generate phrases for numbers < 10000."""
    thousands, hundreds, tens, ones = [int(d) for d in list('%04d' % number)]
    phrase_parts = []

    if thousands:
        phrase_parts.append('%s thousand' % WORDS['digits'][thousands])
    if hundreds:
        phrase_parts.append('%s hundred' % WORDS['digits'][hundreds])
    if (thousands or hundreds) and (tens or ones):
        phrase_parts.append('and')
    if tens:
        if tens == 1:
            phrase_parts.append(WORDS['teens'][10 + ones])
        else:
            phrase_parts.append(WORDS['tens'][tens])
    if ones and tens != 1:
        phrase_parts.append(WORDS['digits'][ones])

    return ' '.join(phrase_parts)


def run():
    start_time = dtime.now()
    total_characters = 0
    highest_number = 1000
    # highest_number = 5

    for number in range(1, highest_number + 1):
        phrase = number_phrase(number)
        total_characters += len(phrase.replace(' ', ''))

    answer = total_characters
    print('answer is: %s' % str(answer))
    print('elapsed seconds: %f' % (dtime.now() - start_time).total_seconds())


if __name__ == '__main__':
    run()
