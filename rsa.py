# prime
import math
from printd import printd
from factors import gcd
from modulus import *


def guess_encryption_key(m):
    """[Try to guess a suitable encryption key by finding something that is coprime]

    Args:
        m ([int]): [The Euler's totient used for the RSA encryption]

    Returns:
        [int]: [a suitable encryption key]
    """
    # https://cacr.uwaterloo.ca/hac/ and https://cacr.uwaterloo.ca/hac/about/chap8.pdf page 291 "8.9 Note (small encryption exponents)"
    return 2 ** 16 + 1


def rsa(p, q, e, plaintext):
    """[from two prime numbers 'p' and 'q' and a private key 'e' calculate the public key]

    Args:
        p ([int]): [a prime number]
        q ([int]): [a prime number]
        e ([int]): [an encryption key coprime with (p-1)*(q-1)) - this will be checked]

    Returns:
        [string]: [The public key will be returned]
    """
    # modulus n:
    n = p * q
    m = (p-1) * (q-1)
    print("p =", p)
    print("q =", q)
    print("n = p * q =", n)
    print("m = (p-1) * (q-1) =", m)
    print("e must be chosen as co-prime with m, you chose e =", e)
    gcd_m_e = math.gcd(m, e)
    if gcd_m_e != 1:
        print("Error: your encryption key e:",
              e, "is not co-prime with m:", m)
        print("Perhaps try a prime number like:", guess_encryption_key(m))
        return None
    else:
        print("Check passed: your encryption key e:", e,
              "has no common factors with m:", m, "so we can proceed...")
    # decryption key d:
    d = mod_mul_inv_euclid(e, m)
    print("decryption key: find d that satisfies: e . d ≅ 1 (mod m)")
    print("decryption key: find d that satisfies:",
          e, ". d ≅ 1 (mod", m, "), d =", d)
    encrypt_decrypt(e, d, n, plaintext)
    return None


def encrypt_decrypt(e, d, n, plaintext):
    """[encrypt and decrypt a number]

    Args:
        e ([type]): [description]
        d ([type]): [description]
        n ([type]): [description]

    Returns:
        [type]: [description]
    """
    # x^e mod n
    x = plaintext
    print("plaintext x:", x)
    print("encrypt: y = x ^ e mod n:", x, "^", e, "mod", n)
    # https://www.geeksforgeeks.org/pow-in-python/ and https://www.geeksforgeeks.org/modular-exponentiation-python/
    encrypted = pow(x, e, n)
    print("encrypted y =", encrypted)
    y = encrypted
    print("decrypt: x = y ^ d mod n:", y, "^", d, "mod", n)
    decrypted = pow(y, d, n)
    print("decrypted x =", decrypted)
    return None
