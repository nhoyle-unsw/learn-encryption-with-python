# factors

import modulus
from printd import printd


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
    printd("find gcd of a , b:", a, ", ", b)
    r = modulus.mod(a, b)
    while (r > 0):
        a = b
        b = r
        r = modulus.mod(a, b)
    return r


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
        r = gcdr(b, modulus.mod(a, b))
    return r
