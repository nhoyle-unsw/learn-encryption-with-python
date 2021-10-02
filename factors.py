# factors

from modulus import mod
from printd import printd, printv


def gcd(a, b):
    """determine the greatest common denominator of two integers.
    https://www.freecodecamp.org/news/euclidian-gcd-algorithm-greatest-common-divisor/
    Pseudo Code of the Algorithm-
    Step 1:  Let  a, b  be the two numbers
    Step 2:  a mod b = R
    Step 3:  Let  a = b  and  b = R
    Step 4:  Repeat Steps 2 and 3 until  a mod b  is greater than 0
    Step 5:  GCD = b
    Step 6: Finish
    """
    printd("find gcd of a , b:", a, ",", b)
    if a == 0 and b == 0:  # gcd of 0 and 0 is 0: https://math.stackexchange.com/questions/495119/what-is-gcd0-0
        return 0
    elif b == 0:  # swap a and b if b is zero otherwise the mod fails.
        printv("swapping a:", a, " with b:", b)
        b = a
        a = 0
        printv("swapped a:", a, " with b:", b)
    r = mod(a, b)
    printd("r:", r, "a:", a, "b:", b)
    while (r > 0):
        a = b
        b = r
        r = mod(a, b)
        printv("r:", r, "a:", a, "b:", b)
    return b  # we return the last remainder found which is b. If no remainder is found at all then the original b is the common factor


def factors(n):
    """[list the factors of two numbers]

    Args:
        n ([int]): [integer to find factors of]

    Returns:
        [String]: [the list of factors of n]
    """
    factors_of_n = ""
    for i in range(1, n // 2 + 1):
        if mod(n, i) == 0:
            factors_of_n += str(i) + " "
    return factors_of_n


def gcdr(a, b):
    """recursively determine the greatest common denominator of two integers.
    https://www.freecodecamp.org/news/euclidian-gcd-algorithm-greatest-common-divisor/
    Pseudo Code of the Algorithm-
    Step 1:  Let  a, b  be the two numbers
    Step 2:  a mod b = R
    Step 3:  Let  a = b  and  b = R
    Step 4:  Repeat Steps 2 and 3 until  a mod b  is greater than 0
    Step 5:  GCD = b
    Step 6: Finish
    """
    printd("find gcd of a , b:", a, ", ", b)
    if b == 0:
        return a
    else:
        r = gcdr(b, mod(a, b))
    return r
