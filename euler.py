# Euler algortims:
# - Totient: # https://learning.oreilly.com/library/view/implementing-cryptography-using/9781119612209/c04.xhtml#head-2-26

from printd import printd
import factors


def phi(n):
    """[summary]

    Args:
        n ([int]): [the number to find Euler's totient for.]

    Returns:
        [int]: [Euler's totient of the number n]
    """
    # We need to find the number of coprimes that a number has so we need to start
    # at 1 and work our way up finding all numbers that have a  greatest common
    # demoninator of 1 wiuth the number (co-prime)
    # https://en.wikipedia.org/wiki/Euler%27s_totient_function
    count = 0
    for i in range(1, n):
        if factors.gcd(i, n) == 1:
            count += 1
    return count
