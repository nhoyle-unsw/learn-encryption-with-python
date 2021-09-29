# Modular arithmetic

## Modulus - Mod
Although it sounds very technical modulus is a pretty simple concept. We all know what division is - how many times a number goes into another number. Well, with integers (whole numbers) when you do division sometimes you have a remainder. e.g. 10 divided by 3 goes 3 times and a remainder of 1. The remainder is the modulus. so:
- 10 mod 3 = 1 (remainder of 1)
- 10 mod 5 = 0 (no remainder)
[1]

### Python code example
```bash
$ python rsa_demo.py mod  -a 10 -b 3        
1

$ python rsa_demo.py mod  -a 10 -b 5        
0
```
**Source code:** https://github.com/nhoyle-unsw/learn-encryption-with-python/blob/main/modulus.py#L12

## Modular multiplicative inverse - Mod Inv
The modular multiplicative inverse is asking the following question:
If I have a number **a** and I want to divide it by **m** to get a remainder of 1, so what would I need to multiply **a** by to get this remainder of 1? 

In maths symbols, it looks like this:
Solve this by finding an x: a**x** = 1 (mod m)

You can do this by trying a mod m, then 2a mod m, then 3a mod m, until you get an answer of 1. Here is an example:
Find the mod inverse 3x = 1 (mod 7)
1. (0 x 3) mod 7 => **0 mod 7** = 0
1. (1 x 3) mod 7 => **3 mod 7** = 3
1. (2 x 3) mod 7 =>** 6 mod 7** = 6
1. (3 x 3) mod 7 => **9 mod 7** = 2
1. (4 x 3) mod 7 => **12 mod 7** = 5
1. (5 x 3) mod 7 => **15 mod 7** = **1** **Yay!** there is no need to go any further, but lets do it anyway:
1. (6 x 3) mod 7 => **18 mod 7** = 4 
1. (7 x 3) mod 7 => **21 mod 7** = 0
1. (8 x 3) mod 7 => **24 mod 7** = 3
1. (9 x 3) mod 7 => **27 mod 7** = 6
1. (10 x 3) mod 7 => **30 mod 7** = 2
1. (11 x 3) mod 7 => **33 mod 7** = 5
1. (12 x 3) mod 36 => **36 mod 7** = **1** **Yay!** no need to go any further, this just repeats the same pattern, so let's do one more:
1. (13 x 3) mod 7 => **39 mod 7** = 4 
1. (14 x 3) mod 7 => **42 mod 7** = 0
1. (15 x 3) mod 7 => **45 mod 7** = 3
1. (16 x 3) mod 7 => **48 mod 7** = 6
1. (17 x 3) mod 7 => **51 mod 7** = 2
1. (18 x 3) mod 7 => **54 mod 7** = 5
1. (19 x 3) mod 7 => **57 mod 7** = **1** **Yay!** no need to go any further. Let's stop here.
(see [2])

### Python code example
```
$ python rsa_demo.py mod -a 3 -b 7
3
$ python rsa_demo.py mod -a 6 -b 7
6
$ python rsa_demo.py mod -a 9 -b 7
2
$ python rsa_demo.py mod -a 12 -b 7        
5
$ python rsa_demo.py mod -a 15 -b 7
1
```
**Source code:** https://github.com/nhoyle-unsw/learn-encryption-with-python/blob/main/modulus.py#L29

## More formal definition
The example defintion above was in order to show a simple algorithm for calulating the multiplicative modular inverse. A more formal definition can be stated as follows [2]:

The modular multiplicative inverse is an integer ‘x’ such that: 

a x ≅ 1 (mod m)

The value of x should be in the range { 1, 2, … m-1}, i.e., in the range of integer modulo m.
(Note that: x cannot be 0 as 0 mod m =0 for all m and will never be 1 )
The multiplicative inverse of “a modulo m” exists if and only if a and m are relatively prime (i.e., if gcd(a, m) = 1). [2]

## My definition
The modular multiplicative inverse is useful in a similar manner to when you multiply the two side of an equation by the same number. It keeps the sides equal. An example is: 

4x = 16  (lets call it equation 1)
so we can work out what x is by putting a number in for x and seeing which one works:
|x|4x|
--- | ---
|1|4| not 16
|2|8| not 16
|3|12| not 16
|4|16| 16 ! So the answer to this equation is x = 4 because it makes the sides equal.

If we start again from the same equation:
4x = 16

But now, let's do something to both sides of the equation. Let's divide each side by 2:
4x/2 = 16/2
2x = 8

Let's divide each side by 2 again:
2x/2 = 8/2
x = 4

Both of these equations are equivalent to the original "equation 1" because x is still equal to 4 even though we divided both sides by 2. You haven't changed anything because you did the same thing to both sides. This is simple to understand for basic arithmetic like multiplication. But for modular arithmetic, it is a little harder to find an equivalent thing we can do to both sides of the equation and still have them equal to each other. So, let's look at the equivalent in modular arithmetic.

I'll use an example equation 10 mod 7. we know that the answer to that is 3 because the remainder is 3. So we can write that 10 mod 7 is congruent to 3 mod 7. This means both 10 and 3 have the same remainder when divided by 7. 10 ÷ 7 = 1 remainder 3. also 3 ÷ 7 = 0 remainder 3. Or 10 mod 7 = 3 and 3 mod 7 = 3 also, so we can write that they are congruent like this:

10 mod 7 ≅ 3 mod 7

Now, what if I want to do multiply both sides of this equation but still have them congruent with each other. How do I find that number? Let's try 2 again and see what happens:

10 X 2 mod 7 = 20 mod 7 = 6
3 x 2  mod 7 = 6  mod 7 = 1  




## References
[1] https://en.wikipedia.org/wiki/Modular_arithmetic
[2] https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/