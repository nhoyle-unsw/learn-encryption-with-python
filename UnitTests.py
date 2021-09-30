import unittest
from modulus import mod, mod_mul_inv_naive
from factors import gcd
from euler import phi
from primes import prime


class UnitTests(unittest.TestCase):

    def test_mod(self):
        self.assertTrue(mod(0, 0) == None)
        self.assertTrue(mod(1, 0) == None)
        self.assertTrue(mod(0, 1) == 0)
        self.assertTrue(mod(0, 10) == 0)
        self.assertTrue(mod(1, 1) == 0)
        self.assertTrue(mod(1, 2) == 1)
        self.assertTrue(mod(2, 1) == 0)
        self.assertTrue(mod(2, 2) == 0)
        self.assertTrue(mod(3, 1) == 0)
        self.assertTrue(mod(3, 2) == 1)
        self.assertTrue(mod(3, 3) == 0)
        self.assertTrue(mod(3, 4) == 3)

    def test_gcd(self):
        self.assertTrue(gcd(0, 0) == 0)
        self.assertTrue(gcd(1, 0) == 1)
        self.assertTrue(gcd(0, 1) == 1)
        self.assertTrue(gcd(0, 2) == 2)
        self.assertTrue(gcd(2, 0) == 2)
        self.assertTrue(gcd(1, 2) == 1)
        self.assertTrue(gcd(2, 1) == 1)
        self.assertTrue(gcd(2, 3) == 1)
        self.assertTrue(gcd(3, 2) == 1)
        self.assertTrue(gcd(4, 0) == 4)
        self.assertTrue(gcd(4, 1) == 1)
        self.assertTrue(gcd(1, 4) == 1)
        self.assertTrue(gcd(4, 2) == 2)
        self.assertTrue(gcd(4, 3) == 1)
        self.assertTrue(gcd(4, 4) == 4)
        self.assertTrue(gcd(4, 5) == 1)
        self.assertTrue(gcd(4, 6) == 2)
        self.assertTrue(gcd(4, 7) == 1)
        self.assertTrue(gcd(4, 8) == 4)
        self.assertTrue(gcd(8, 4) == 4)
        self.assertTrue(gcd(4, 9) == 1)
        self.assertTrue(gcd(9, 4) == 1)
        self.assertTrue(gcd(4, 10) == 2)
        self.assertTrue(gcd(10, 4) == 2)
        self.assertTrue(gcd(13, 17) == 1)

    def test_phi(self):
        self.assertTrue(phi(0) == 0)
        self.assertTrue(phi(1) == 1)
        self.assertTrue(phi(2) == 1)
        self.assertTrue(phi(3) == 2)
        self.assertTrue(phi(4) == 2)
        self.assertTrue(phi(5) == 4)
        self.assertTrue(phi(6) == 2)
        self.assertTrue(phi(7) == 6)
        self.assertTrue(phi(8) == 4)
        self.assertTrue(phi(9) == 6)

    def test_prime(self):
        self.assertFalse(prime(-11))
        self.assertFalse(prime(-10))
        self.assertFalse(prime(-7))
        self.assertFalse(prime(-4))
        self.assertFalse(prime(-3))
        self.assertFalse(prime(-2))
        self.assertFalse(prime(-1))
        self.assertFalse(prime(0))
        self.assertFalse(prime(1))
        self.assertFalse(prime(0))
        self.assertFalse(prime(4))
        self.assertFalse(prime(6))
        self.assertFalse(prime(10))
        self.assertFalse(prime(22))
        self.assertFalse(prime(24))
        self.assertFalse(prime(100))
        self.assertFalse(prime(102))
        self.assertTrue(prime(2))
        self.assertTrue(prime(3))
        self.assertTrue(prime(7))
        self.assertTrue(prime(11))
        self.assertTrue(prime(13))
        self.assertTrue(prime(17))
        self.assertTrue(prime(19))
        self.assertTrue(prime(23))
        self.assertTrue(prime(101))
        self.assertTrue(prime(103))

    def test_mod_mult_inv(self):
        # https://www.wolframalpha.com/input/?i=0x+%3D+1+%28mod+1%29
        # self.assertTrue(mod_mul_inv_naive(0, 1) == 0) # Todo: I think these are only defined for >1, need to find reference
        # self.assertTrue(mod_mul_inv_naive(1, 1) == 1) # Todo: I think these are only defined for >1, need to find reference
        self.assertTrue(mod_mul_inv_naive(3, 7) == 5)
        # https://www.wolframalpha.com/input/?i=7x+%3D+1+%28mod+42%29
        self.assertTrue(mod_mul_inv_naive(7, 42) == None)
        # https://www.wolframalpha.com/input/?i=3x+%3D+1+%28mod+3%29
        self.assertTrue(mod_mul_inv_naive(3, 3) == None)


if __name__ == '__main__':
    unittest.main()
