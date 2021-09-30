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
        printd("can not divide by zero, b:", b)
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


def mod_mul_inv_naive(a, m):
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
    printd("ax = 1 (mod m): %ix = 1 (mod %i)" % (a, m))
    for x in range(0, m+1):
        printd("mod inv, try x=", x)
        if(mod(a*x, m)) == 1:
            return x
    return None


def mod_mul_inv_euclid(a, m):
    """Using the Extended Euclidian Algorithm: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    Euclidean Algorithm: https://www.youtube.com/watch?v=p5gn2hj51hs
    Extended Euclidean Algorithm: https://www.youtube.com/watch?v=hB34-GSDT3k
    Multiplicative inverse mod n: https://www.youtube.com/watch?v=_bRVA5b4sb4

    Args:
        a ([int]): [integer a (which is coprime with m) to find the modular multiplicative inverse of]
        m ([int]): [the modulus (which is coprime with a)]

    Returns:
        [x]: [the modular multiplicative inverse of a]
    """
    # ToDo: implement this when you have time
    x = 0
    newx = 1
    r = m
    newr = a

    while newr != 0:
        quotient = r // newr
        printd("quotient = r // newr = ", r, "//", newr, "=", quotient)
        (x, newx) = (newx, x - (quotient * newx))
        (r, newr) = (newr, r - (quotient * newr))
        printd("newr =", newr)

    printd("r =", r)
    if r > 1:
        return "a is not invertible"
    printd("x =", r)
    if x < 0:
        x = x + m
        printd("x =", r)
    return x


def mod_mul_inv_euler(a, m):
    """Using Euler's Theorem: https://en.wikipedia.org/wiki/Euler%27s_theorem
    and Totient function: https://en.wikipedia.org/wiki/Euler%27s_totient_function 
    calculating: https://www.quora.com/How-do-I-calculate-8-%E2%80%931-mod-77-using-Eulers-Theorem?share=1 

    Args:
        a ([int]): [the coprime with m or just plain old prime integer to find the modular multiplicative inverse of]
        m ([int]): [the modulus (when coprime with a)]

    Returns:
        [x]: [the modular multiplicative inverse of a (prime)]
    """
    # ToDo: implement this when you have time
    return None
