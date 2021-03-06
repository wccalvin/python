#!/usr/local/bin/python3


def checkio(array):
    """
    sums even-indexes elements and multiply at the last
    """
    if len(array) != 0:
        sum_even = sum(array[::2])
        return sum_even * array[-1]
    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
