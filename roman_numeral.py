from math import ceil, log10

#
# Library with helper functions related to Roman Numerals
#

# Hardcoded representations of specific benchmark numbers
ROMANS = [
    ('I',    1),
    ('IV',   4),
    ('V',    5),
    ('IX',   9),
    ('X',   10),
    ('XL',  40),
    ('L',   50),
    ('XC',  90),
    ('C',  100),
    ('CD', 400),
    ('D',  500),
    ('CM', 900),
    ('M', 1000)
]
ROMAN_STRS = list(map(lambda p: p[0], ROMANS))
ROMAN_VALS = list(map(lambda p: p[1], ROMANS))


def roman_numeral_to_value(s: str) -> int:
    """
    Given a string `s` assumed to be a valid (not-necessarily-minimal)
      number written in Roman numeral form,
      return the number represented by `s`.

    Args:
        s (str): Roman numeral representation of some number in uppercase

    Returns:
        (int): Number represented by roman numeral string `s`

    Raises:
        AssertError: if incorrect args are given
        ValueError:  if `s` cannot be parsed into value
    """
    assert type(s) == str and s.isupper()

    global ROMAN_STRS, ROMAN_VALS
    val = 0

    # Step backwards through hardcoded symbols, siphoning off amounts into `val`
    i = len(ROMAN_STRS)-1  # Index into ROMAN_* lists
    j = 0                  # Index into `s`
    while j < len(s) and i >= 0:
        if s[j:].startswith(ROMAN_STRS[i]):
            j += len(ROMAN_STRS[i])
            val += ROMAN_VALS[i]
        else:
            i -= 1

    if j < len(s):
        # Something wasn't recognized
        raise ValueError('Invalid Roman numeral {}'.format(s))
    else:
        return val


def roman_numeral_from_value(n: int) -> str:
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

    global ROMAN_STRS, ROMAN_VALS
    s = []

    # Figure out where to start siphoning
    i = min(4 * ceil(log10(n)), len(ROMAN_VALS)-1)  # Index into ROMAN_*
    while i >= 0 and n > 0:
        if n >= ROMAN_VALS[i]:
            s.append(ROMAN_STRS[i])
            n -= ROMAN_VALS[i]
        else:
            i -= 1

    return ''.join(s)
