# Problem 89:
#     Roman Numerals
#
# Description:
#     For a number written in Roman numerals to be considered valid there are basic rules which must be followed.
#     Even though the rules allow some numbers to be expressed in more than one way
#       there is always a "best" way of writing a particular number.
#
#     For example, it would appear that there are at least six ways of writing the number sixteen:
#
#         IIIIIIIIIIIIIIII
#         VIIIIIIIIIII
#         VVIIIIII
#         XIIIIII
#         VVVI
#         XVI
#
#     However, according to the rules only XIIIIII and XVI are valid,
#       and the last example is considered to be the most efficient,
#       as it uses the least number of numerals.
#
#     The 11K text file, roman.txt (right click and 'Save Link/Target As...'),
#       contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals;
#       see `About... Roman Numerals` [https://projecteuler.net/about=roman_numerals]
#       for the definitive rules for this problem.
#
#     Find the number of characters saved by writing each of these in their minimal form.
#
#     Note: You can assume that all the Roman numerals in the file
#           contain no more than four consecutive identical units.

from roman_numeral import *


def main(filename: str) -> int:
    """
    Returns the number of characters saved by writing the not-necessarily-minimal
      Roman numeral numbers in `filename` in minimal form.

    Args:
        filename (str): File containing not-necessarily-minimal Roman numerals

    Returns:
        (int): Number of characters saved by writing Roman numerals in `filename` in minimal form.

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(filename) == str

    saved = 0

    with open(filename, 'r') as f:
        for line in f:
            roman_raw = line.strip()
            roman_val = roman_numeral_to_value(roman_raw)
            roman_clean = roman_numeral_from_value(roman_val)
            saved += (len(roman_raw) - len(roman_clean))

    return saved


if __name__ == '__main__':
    roman_numerals_filename = 'roman.txt'
    saved_characters = main(roman_numerals_filename)
    print('Number of characters saved by writing Roman numerals in {} in minimal form:'.format(roman_numerals_filename))
    print('  {}'.format(saved_characters))
