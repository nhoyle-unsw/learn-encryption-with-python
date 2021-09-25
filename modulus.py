# modulus
# https://en.wikipedia.org/wiki/Modular_arithmetic
# https://en.wikipedia.org/wiki/Modulo_operation
# https://www.geeksforgeeks.org/modular-division/
# https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic
# https://www.pythoncentral.io/python-null-equivalent-none/
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem

from printd import printd


def mod(a, b):
    """find a mod b."""
    printd("find a mod b:", a, "mod", b)
    if b == 0:
        # can not divide by zero
        return None
    # start at the value of a
    r = a
    # chack if our remainder is still larger than b
    while r >= b:
        printd("remainder:", r)
        # subtract the divisor
        r = r - b
    printd("a mod b =", r)
    return r


def mod_mul_inv(a, m):
    """[summary]
    find the modular multiplicative inverse of a number a in modulo m
    https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
    "Extended Euclidean algorithm - A modular multiplicative inverse of a modulo m can be found by using the extended Euclidean algorithm."
    "Using Euler's theorem - As an alternative to the extended Euclidean algorithm, Euler's theorem may be used to compute modular inverses."

    Args:
        a ([int]): [the integer to find the modular multiplicative inverse of]
        m ([int]): [the modulus]

    Returns:
        [x]: [the modular multiplicative inverse of a]
    """
    return None
