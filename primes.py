# prime

from printd import printd
from factors import gcd
from modulus import mod


def prime(n):
    """[summary]

    Args:
        n ([int]): [number to test for primeness]

    Returns:
        [boolean]: [True when prime False otherwise]
    """
    # A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers.
    # https://en.wikipedia.org/wiki/Prime_number

    # first checck it is greater than 1
    printd("Check if n is prime:", n)
    if not n > 1:
        return False
    count = 0
    for i in range(2, n):  # 0 -> n-1
        printd("i:", i)
        if mod(n, i) == 0:
            return False
    return True
