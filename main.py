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

def get_roman_numeral_val(s: str) -> int:
    """
    Given a string `s` assumed to be a valid (not-necessarily-minimal)
      number written in Roman numeral form,
      return the value represented by `s`.

    Args:
        s (str): Roman numeral representation of some number in uppercase

    Returns:
        (int): Numerical value represented by roman numeral string `s`

    Raises:
        AssertError: if incorrect args are given
        ValueError:  if `s` cannot be parsed into value
    """
    assert type(s) == str and s.isupper()

    val = 0

    # Walk through string, adding onto `val`
    i = 0
    while i < len(s):
        if s[i] == 'M':  # Standalone 'M'
            i += 1
            val += 1000
        elif s[i] == 'D':  # Standalone 'D'
            i += 1
            val += 500
        elif s[i] == 'C':
            # Need to check for combinations
            if i+1 < len(s):
                if s[i+1] == 'M':  # Combo 'CM'
                    i += 2
                    val += 900
                elif s[i+1] == 'D':  # Combo 'CD'
                    i += 2
                    val += 400
                else:  # Standalone 'C'
                    i += 1
                    val += 100
            else:
                # 'C' is at end of str, no tricks
                i += 1
                val += 100
        elif s[i] == 'L':  # Standalone 'L'
            i += 1
            val += 50
        elif s[i] == 'X':
            # Need to check for combinations
            if i+1 < len(s):
                if s[i+1] == 'C':  # Combo 'XC'
                    i += 2
                    val += 90
                elif s[i+1] == 'L':  # Combo 'XL'
                    i += 2
                    val += 40
                else:  # Standalone 'X'
                    i += 1
                    val += 10
            else:
                # 'X' is at end of str, no tricks
                i += 1
                val += 10
        elif s[i] == 'V':  # Standalone 'V'
            i += 1
            val += 5
        elif s[i] == 'I':
            # Need to check for combinations
            if i+1 < len(s):
                if s[i+1] == 'X':  # Combo 'IX'
                    i += 2
                    val += 9
                elif s[i+1] == 'V':  # Combo 'IV'
                    i += 2
                    val += 4
                else:  # Standalone I
                    i += 1
                    val += 1
            else:
                # 'I' is at end of str, no tricks
                i += 1
                val += 1
        else:
            # Unrecognized char
            raise ValueError('Invalid char "{}" in Roman numeral'.format(s[i]))

    return val


def get_roman_numeral_str(n: int) -> str:
    """
    Returns the minimal Roman numeral representation of `n`.

    Args:
        n (int): Natural number

    Returns:
        (str): Minimal Roman numeral representation of `n`

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 0

    s = []

    # Siphon off thousands into M's
    while n >= 1000:
        s.append('M')
        n -= 1000

    # Special cases of 100's
    if n >= 900:
        s.append('CM')
        n -= 900
    elif n >= 500:
        s.append('D')
        n -= 500
    elif n >= 400:
        s.append('CD')
        n -= 400
    else:
        pass

    # Siphon off remaining hundreds into C's
    while n >= 100:
        s.append('C')
        n -= 100

    # Special cases of 10's
    if n >= 90:
        s.append('XC')
        n -= 90
    elif n >= 50:
        s.append('L')
        n -= 50
    elif n >= 40:
        s.append('XL')
        n -= 40
    else:
        pass

    # Siphon off remaining tens into X's
    while n >= 10:
        s.append('X')
        n -= 10

    # Special cases of 1's
    if n == 9:
        s.append('IX')
        n = 0
    elif n >= 5:
        s.append('V')
        n -= 5
    elif n == 4:
        s.append('IV')
        n = 0
    else:
        pass

    # Siphon off remaining ones into I's
    s.append('I' * n)

    # Put everything together
    return ''.join(s)


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
            roman_val = get_roman_numeral_val(roman_raw)
            roman_clean = get_roman_numeral_str(roman_val)
            saved += (len(roman_raw) - len(roman_clean))

    return saved


if __name__ == '__main__':
    roman_numerals_filename = 'roman.txt'
    saved_characters = main(roman_numerals_filename)
    print('Number of characters saved by writing Roman numerals in {} in minimal form:'.format(roman_numerals_filename))
    print('  {}'.format(saved_characters))
