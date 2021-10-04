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
    print("math.gcd(m, e)=", gcd_m_e)
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
    x = plaintext
    encrypted = encrypt(x, e, n)
    y = encrypted
    decrypted = decrypt(y, d, n)
    if(decrypted != plaintext):
        print("Error: unable to encrypt/decrypt without loss. Your plaintext needs to be less than n:", n)
    return y


def encrypt(plaintext, e, n):
    """[encrypt a message]

    Args:
        plaintext ([int]): [The plaintext to be encrypted]
        e ([int]): [The encryption key]
        n ([int]): [modulus]


    Returns:
        [int]: [y = ciphertext]
    """
    x = plaintext
    print("plaintext x:", x)
    print("ciphertext: y = x ^ e mod n:", x, "^", e, "mod", n)
    # https://www.geeksforgeeks.org/pow-in-python/ and https://www.geeksforgeeks.org/modular-exponentiation-python/
    y = pow(x, e, n)
    print("ciphertext y =", y)
    return y


def decrypt(ciphertext, d, n):
    """[decrypt a message]

    Args:
        ciphertext ([int]): [The ciphertext to be decrypted]
        d ([int]): [The decryption key]
        n ([int]): [modulus]

    Returns:
        [int]: [x = plaintext]
    """
    y = ciphertext
    print("ciphertext y to decrypt =", y)
    print("decrypt: x = y ^ d mod n:", y, "^", d, "mod", n)
    x = pow(y, d, n)
    print("plaintext x =", x)
    return x
