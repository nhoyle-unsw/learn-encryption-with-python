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
    return None
