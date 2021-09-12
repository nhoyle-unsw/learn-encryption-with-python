# Euler's Totient Function

Euler investigated the distribution of prime numbers

## Phi function φ(n)

Phi is a Greek letter pronounce "fai"
The phi function defines how many numbers less than any integer N that do not share any common factor with it.

**e.g. to calculate the phi of 8 or φ(8)**

1. Write down all the numbers from one to eight:
   1
   2
   3
   4
   5
   6
   7
   8
1. Find any common factors those numbers have with eight and cross them out
   1
   ~~2~~
   3
   ~~4~~
   5
   ~~6~~
   7
   8
1. Count the numbers that dont have common factors: 4
1. That is your answer: φ(8) = 4

This is quite a diffcult thing to calcuate for large numbers becuase you have to go through all of the numbers and find factors that match.

However, it is easy to fin the Phi of a prime number. Becuase prime numbers don not share factors with any other numbers then the Phi of a prim number has to be one less than the prim number. You can see this by trying the abve stepps for the number seven. Let's do that now:

**e.g. to calculate the Phi of 7 or φ(7)**

1. Write down all the numbers from one to eight:
   1
   2
   3
   4
   5
   6
   7
1. Find any common factors those numbers have with eight and cross them out
   ~~1~~
   ~~2~~
   ~~3~~
   ~~4~~
   ~~5~~
   ~~6~~
   7
1. Count the numbers that dont have common factors: 6
1. That is your answer: φ(7) = 6

Becuase all prime numbers do not have common factors with othernumbers the Phi of a prime number will always be one less than the prime number. So if we repersent a prime numbers as the letter p, then we can say ht Phi of p is p minus one, or:

φ(p) = p-1

**e.g. Phi of 21377 (which is a prime number) is 21376. Easy!**

## Why is this important to RSA encryption?

RSA encryption uses a relationship between two prime numbers and the totient of those prime numbers to create the encryption and decryption keys:

- The encryption key uses the result of p multiplied by q: p.q
- The decryption key uses the result of the Phi of p multiplied by the Phi of q: φ(p) . φ(q)

The magic thing about φ(p) . φ(q) is that it is the same as φ(p.q)

**e.g. the Phi of 7 is 6 and the Phi of 11 is 10, the Phi of 7 times 11 is Phi of 77 which equal 60.**

## Phi of all number plotted on a graph

![Integers, Factoring and Prime Numbers](https://raw.githubusercontent.com/wiki/nhoyle-unsw/learn-encryption-with-python/images/plot-phi-of-x.png)

## Mathematics

φ(p.q) = φ(p) . φ(q)

So, if we know a number N that is the product of two primes:
N=p.q

Then we also know that:

φ(N) = φ(p) . φ(q)

And since we know that the Phi of a prime number is the number minus one, then:
φ(N) = (p-1) . (q-1)

We will use this property of two prime numbers and their product later when calculating RSA encryption and decryption.
