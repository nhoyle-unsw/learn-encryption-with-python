# prime

from printd import printd
from factors import gcd
from modulus import mod, mod_mul_inv_naive


def guess_encryption_key(m):
    """[Try to guess a suitable encryption key by finding something that is coprime]

    Args:
        m ([int]): [The Euler's totient used for the RSA encryption]

    Returns:
        [int]: [a suitable encryption key]
    """
    return 37


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
    print("n:", n)
    print("m:", m)
    print("e:", e)
    if gcd(m, e) != 1:
        print("Error: your encryption key e:",
              e, "is nopt co-prime with m:", m)
        print("Perhaps try a prime number like:", guess_encryption_key(m))
        return None
    d = mod_mul_inv_naive(e, m)
    print("d:", d)
    encrypt_decrypt(e, d, n, plaintext)
    return d


def encrypt_decrypt(e, d, n, plaintext):
    """[encrypt and decrypt a number]

    Args:
        e ([type]): [description]
        d ([type]): [description]
        n ([type]): [description]

    Returns:
        [type]: [description]
    """
    # x^e  nod n
    x = plaintext
    print("plaintext x:", x)
    print("encrypt: x ^ e mod n:", x, "^", e, "mod", n)
    print("python check:", (x ^ e) % n)
    encrypted = mod(x ^ e, n)
    print("encrypted:", encrypted)
    y = encrypted
    decrypted = mod(y ^ d, n)
    print("decrypted:", decrypted)
    return None
