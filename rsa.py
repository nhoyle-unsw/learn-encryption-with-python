# prime
import math
from printd import printd
from factors import gcd
from modulus import *
import converter


def guess_encryption_key(m):
    """[Try to guess a suitable encryption key by finding something that is coprime]

    Args:
        m ([int]): [The Euler's totient used for the RSA encryption]

    Returns:
        [int]: [a suitable encryption key]
    """
    # https://cacr.uwaterloo.ca/hac/ and https://cacr.uwaterloo.ca/hac/about/chap8.pdf page 291 "8.9 Note (small encryption exponents)"
    return 2 ** 16 + 1


def rsa(p, q, e):
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
    """
    x = plaintext
    encrypted = encrypt(x, e, n)
    y = encrypted
    decrypted = decrypt(y, d, n)
    if(decrypted != plaintext):
        print("Error: unable to encrypt/decrypt without loss. Your plaintext needs to be less than n:", n)
    return y
    """
    return None


def encrypt(plaintext_number, e, n):
    """[encrypt a plaintext_number]

    Args:
        plaintext_number ([int]): [The plaintext number to be encrypted]
        e ([int]): [The encryption key]
        n ([int]): [modulus]


    Returns:
        [int]: [y = ciphertext]
    """
    x = plaintext_number
    printd("plaintext_number x:", x)
    printd("ciphertext_number: y = x ^ e mod n:", x, "^", e, "mod", n)
    # https://www.geeksforgeeks.org/pow-in-python/ and https://www.geeksforgeeks.org/modular-exponentiation-python/
    y = pow(x, e, n)
    printd("ciphertext_number y =", y)
    return y


def decrypt(ciphertext_number, d, n):
    """[decrypt a message]

    Args:
        ciphertext_number ([int]): [The ciphertext number to be decrypted]
        d ([int]): [The decryption key]
        n ([int]): [modulus]

    Returns:
        [int]: [x = plaintext]
    """
    y = ciphertext_number
    printd("ciphertext_number y to decrypt =", y)
    printd("decrypt: x = y ^ d mod n:", y, "^", d, "mod", n)
    x = pow(y, d, n)
    printd("plaintext x =", x)
    return x


def encrypt_large_string(large_string, e, n):
    encrypted = ""
    numbers_as_int_list, numbers_as_string = converter.convert_to_numbers(
        large_string)
    for number_as_int in numbers_as_int_list:
        encrypted += str(encrypt(int(number_as_int), e, n)) + "\n"
    return encrypted


def encrypt_file_contents(input_file_name_plaintext_chars, e, n):
    large_string = read_file(input_file_name_plaintext_chars)
    large_string_encrypted = encrypt_large_string(large_string, e, n)
    return large_string_encrypted


def read_file(file_name):
    text_file = open(file_name)
    data = text_file.read()
    printd("file contents:[" + data + "]")
    text_file.close()
    return data


def decrypt_large_string(large_string, e, n):
    decrypted = ""
    # remove new lines
    # https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_join2
    for number_as_string in large_string.split("\n"):
        # avoid blank lines
        if len(number_as_string) > 0:
            decrypted += str(decrypt(int(number_as_string), e, n))
    decrypted_converted = converter.convert_to_text(decrypted)
    return decrypted_converted


def decrypt_file_contents(input_file_name_ciphertext_numbers, d, n):
    large_string = read_file(input_file_name_ciphertext_numbers)
    large_string_decrypted = decrypt_large_string(
        large_string, d, n)
    return large_string_decrypted
