# Entrypoint for running the RSA demonstration algorithms
# commands are executed like this:
# rsa_demo gcd 26 7
# rsa_demo 2 mod
# rsa_demo mod_inverse
# rsa_demo eulers_totient
#
import sys
import argparse
from printd import printd
from printd import printv
import printd as printd_module
import modulus
import factors
import euler
import primes
import rsa
import converter

REAL_FILENAME = "confession_real.txt"
REAL_FILE_SHA256 = "ee2b34b775d70cd1e23ff42a7ed39731419a443c4f08b062e96015e6e951588d"

FAKE_FILENAME = "confession_fake.txt"
FAKE_FILE_SHA256 = "44026d38d615a11633ed19548eeaea15b38e99fcc670277a42c80a5edc26df11"

parser = argparse.ArgumentParser()
parser.add_argument(
    "command", help="""the command you want to run:   \n
       gcd -a -b,   \n
       factors -n 24,   \n
       mod -a 10 -b 3,   \n
       modinv -a 3 -m 7,   \n
       modinv_euclid -a 3 -m 7,   \n
       phi -n 13,   \n
       rsa -p 557 -q 839 -e 7825,   \n
       rsa-encrypt -x 181901 -e 7825 -n 467323,   \n
       rsa-decrypt -y 183780 -d 214833 -n 467323,   \n
       encrypt_and_decrypt_file_contents -e 65537 -d 282558858218830016898995928393 -n 990376505031955291131092008489 -f plaintext_long_length.txt
       """)
parser.add_argument("-a", type=int,
                    help="value for a - in a mod b")
parser.add_argument("-b", type=int,
                    help="value for b - in a mod b")
parser.add_argument("-n", type=int,
                    help="value for n - in factors or phi")
parser.add_argument("-m", type=int,
                    help="value for m - in mod inverse a mod m")
parser.add_argument("-p", type=int,
                    help="value for p - prime number")
parser.add_argument("-q", type=int,
                    help="value for q - prime number")
parser.add_argument("-e", type=int,
                    help="value for e - encryption key")
parser.add_argument("-d", type=int,
                    help="value for d - decryption key")
parser.add_argument("-x", type=int,
                    help="value for x - plainttext as an integer")
parser.add_argument("-y", type=int,
                    help="value for y - ciphertext as an integer")
parser.add_argument("-t",
                    help="value for t - text to be converted to numbers")
parser.add_argument("-f",
                    help="value for f - file to be encrypted or decrypted")
parser.add_argument("-D", "--debug", action="store_true",
                    help="Output debug statements (you need to press Enter to see each line of the output)")
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
is_debug = args.debug or args.verbose
is_verbose = args.verbose
# https://stackoverflow.com/questions/38246928/using-global-variable-in-python-among-modules-in-different-packages
# set the debug and verbosity levels in the print module
printd_module.is_debug = args.debug or args.verbose
printd_module.is_verbose = args.verbose


def main():
    printd('Number of arguments:', len(sys.argv), 'arguments.')
    printd('Argument List:', str(sys.argv))
    printv('Verbose output:')
    if "mod" == args.command:
        print(modulus.mod(args.a, args.b))
        return 0
    if "power_mod" == args.command:
        print(pow(args.a, args.b, args.n))
        return 0
    elif "modinv" == args.command:
        print(modulus.mod_mul_inv_naive(args.a, args.m))
        return 0
    elif "modinv_euclid" == args.command:
        print(modulus.mod_mul_inv_euclid(args.a, args.m))
        return 0
    elif "modinv_euler" == args.command:
        print(modulus.mod_mul_inv_euler(args.a, args.m))
        return 0
    elif "factors" == args.command:
        print(factors.factors(args.n))
        return 0
    elif "gcd" == args.command:
        print(factors.gcd(args.a, args.b))
        return 0
    elif "gcdr" == args.command:
        print(factors.gcdr(args.a, args.b))
        return 0
    elif "prime" == args.command:
        print(primes.prime(args.n))
        return 0
    elif "phi" == args.command:
        print(euler.phi(args.n))
        return 0
    elif "rsa" == args.command:
        rsa.rsa(args.p, args.q, args.e)
        return 0
    elif "rsa-encrypt" == args.command:
        print(rsa.encrypt(args.x, args.e, args.n))
        return 0
    elif "rsa-decrypt" == args.command:
        print(rsa.decrypt(args.y, args.d, args.n))
        return 0
    elif "convert_to_number" == args.command:
        _, text_as_numbers = converter.convert_to_numbers(args.t)
        print(text_as_numbers)
        return 0
    elif "convert_to_text" == args.command:
        print(converter.convert_to_text(args.t))
        return 0
    elif "encrypt_large_string" == args.command:
        print(rsa.encrypt_large_string(args.t, args.e, args.n))
        return 0
    elif "decrypt_large_string" == args.command:
        print(rsa.decrypt_large_string(args.t, args.d, args.n))
        return 0
    elif "encrypt_file_contents" == args.command:
        print(rsa.encrypt_file_contents(args.f, args.e, args.n))
        return 0
    elif "decrypt_file_contents" == args.command:
        print(rsa.decrypt_file_contents(args.f, args.d, args.n))
        return 0
    elif "encrypt_and_decrypt_file_contents" == args.command:
        print("====== Start")
        if not args.n > 2.56 * 10**(30-1):
            # Our largest character is 255, so if every one of the ten characters is
            # made up of that charctr then it can be no bigger than:
            # 255,255,255,255,255,255,255,255,255,255 so any 'n' larger than
            # 256,000,000,000,000,000,000,000,000,000 should work
            print("Error: Please supply a modulus n larger than 30 digits. Exiting.")
            return 1
        print("Plaintext file contents - [ and ] are not part of the file:")
        plaintext_file_contents = rsa.read_file(args.f)
        print("[" + plaintext_file_contents + "]")
        print("======")

        print("Encoded contents - [ and ] are not part of the file:")
        numbers_as_int_list, numbers_as_string = converter.convert_to_numbers(
            plaintext_file_contents)
        print("[" + numbers_as_string + "]")
        print("======")

        print("RSA Encrypted contents using public key",
              args.e, "- [ and ] are not part of the file:")
        encryption_result = rsa.encrypt_file_contents(args.f, args.e, args.n)
        print("[" + encryption_result + "]")
        print("======")

        print("RSA Decrypted contents using private key",
              args.d, "-[ and ] are not part of the file:")
        decryption_result = rsa.decrypt_large_string(
            encryption_result, args.d, args.n)
        print("[" + decryption_result + "]")
        print("======")

        print("Checking if original plaintext matches encrypted + decrypted result:")
        if plaintext_file_contents == decryption_result:
            print("original file: [" + plaintext_file_contents + "]")
            print("encr and decr: [" + decryption_result + "]")
            print("Both Match!")
        else:
            print(
                "Error: They don't match! You may have found a bug. Please report it here: ")
            print(
                "https://github.com/nhoyle-unsw/learn-encryption-with-python/issues/new")

        print("====== End")
        return 0


if __name__ == "__main__":
    main()
