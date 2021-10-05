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
    "command", help="""the command you want to run: \n
       gcd -a -b \n
       factors -n 24
       mod -a 10 -b 3 \n
       modinv -a 3 -m 7 \n
       modinv_euclid -a 3 -m 7 \n
       phi -n 13
       rsa -p 557 -q 839 -e 7825 -x 181901\n
       rsa-encrypt -x 181901 -e 7825 -n 467323 
       rsa-decrypt -y 183780 -d 214833 -n 467323
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
                    help="value for t - text to be converted to an integer")
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
        rsa.rsa(args.p, args.q, args.e, args.x)
        return 0
    elif "rsa-encrypt" == args.command:
        rsa.encrypt(args.x, args.e, args.n)
        return 0
    elif "rsa-decrypt" == args.command:
        rsa.decrypt(args.y, args.d, args.n)
        return 0
    elif "convert_to_number" == args.command:
        converter.convert_to_number(args.t)
        return 0
    elif "convert_to_text" == args.command:
        converter.convert_to_text(args.t)
        return 0
    elif "encrypt_large_string" == args.command:
        rsa.encrypt_large_string(args.t)
        return 0
    elif "decrypt_large_string" == args.command:
        rsa.decrypt_large_string(args.t)
        return 0
    elif "encrypt_file_contents" == args.command:
        rsa.encrypt_file_contents(args.t)
        return 0
    elif "decrypt_file_contents" == args.command:
        rsa.decrypt_file_contents(args.t)
        return 0


if __name__ == "__main__":
    main()
