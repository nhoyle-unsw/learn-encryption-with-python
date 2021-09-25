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
import modulus
import factors
import euler

REAL_FILENAME = "confession_real.txt"
REAL_FILE_SHA256 = "ee2b34b775d70cd1e23ff42a7ed39731419a443c4f08b062e96015e6e951588d"

FAKE_FILENAME = "confession_fake.txt"
FAKE_FILE_SHA256 = "44026d38d615a11633ed19548eeaea15b38e99fcc670277a42c80a5edc26df11"

parser = argparse.ArgumentParser()
parser.add_argument(
    "command", help="the command you want to run: mod, gcd, mod_mul_inv")
parser.add_argument("-a", type=int,
                    help="value for a")
parser.add_argument("-b", type=int,
                    help="value for b")
parser.add_argument("-n", type=int,
                    help="value for n")
parser.add_argument("-d", "--debug", action="store_true",
                    help="Output debug statements (you need to press Enter to see each line of the output)")
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
is_debug = args.debug


def main():
    printd('Number of arguments:', len(sys.argv), 'arguments.')
    printd('Argument List:', str(sys.argv))
    if "mod" == args.command:
        print(modulus.mod(args.a, args.b))
        return 0
    elif "gcd" == args.command:
        print(factors.gcd(args.a, args.b))
        return 0
    elif "gcdr" == args.command:
        print(factors.gcdr(args.a, args.b))
        return 0
    elif "phi" == args.command:
        print(euler.phi(args.n))
        return 0


if __name__ == "__main__":
    main()
