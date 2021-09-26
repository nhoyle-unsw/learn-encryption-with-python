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
    # check if our remainder is still larger than b
    while r >= b:
        printd("remainder:", r)
        # subtract the divisor
        r = r - b
    printd("a mod b =", r)
    return r


def mod_mul_inv_naieve(a, m):
    """[summary]
    find the modular multiplicative inverse of a number a in modulo m
    https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
    "Extended Euclidean algorithm - A modular multiplicative inverse of a modulo m can be found by using the extended Euclidean algorithm."
    "Using Euler's theorem - As an alternative to the extended Euclidean algorithm, Euler's theorem may be used to compute modular inverses."
    https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
    Find an x where: ax = 1 (mod m) e.g.:
    6x = 1 (mod 23) : x=4 makes this true
    "A Naive method is to try all numbers from 1 to m. For every number x, check if (a*x)%m is 1."

    Args:
        a ([int]): [the integer to find the modular multiplicative inverse of]
        m ([int]): [the modulus]

    Returns:
        [x]: [the modular multiplicative inverse of a]
    """
    for i in range(1, m):
        if (mod(mod(a, i) * mod(i, m), m) == 1):
            return i
    return -1


def mod_mul_inv_euclid(a, m):
    """Using the Extended Euclidian Algorithm: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm

    Args:
        a ([int]): [integer a (which is coprime with m) to find the modular multiplicative inverse of]
        m ([int]): [the modulus (which is coprime with a)]

    Returns:
        [x]: [the modular multiplicative inverse of a]
    """
    # ToDo: implement this when you have time
    return None


def mod_mul_inv_euler(a, m):
    """Using Euler's Theorem: https://en.wikipedia.org/wiki/Euler%27s_theorem
    and Totient function: https://en.wikipedia.org/wiki/Euler%27s_totient_function 

    Args:
        a ([int]): [the coprime with m or just plain old prime integer to find the modular multiplicative inverse of]
        m ([int]): [the modulus (when coprime with a)]

    Returns:
        [x]: [the modular multiplicative inverse of a (prime)]
    """
    # ToDo: implement this when you have time
    return None
