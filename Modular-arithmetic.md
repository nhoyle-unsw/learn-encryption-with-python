# Modular arithmetic

## Mod
Although it sounds very technical modulus is a pretty simple concept. We all know what division is - how many times a number goes into another number. Well, with integers (whole numbers) when you do division sometimes you have a remainder. e.g. 10 divided by 3 goes 3 times and a remainder of 1. The remainder is the modulus. so:
- 10 mod 3 = 1 (remainder of 1)
- 10 mod 5 = 0 (no remainder)

### Python code example
```bash
$ python rsa_demo.py mod  -a 10 -b 3        
1

$ python rsa_demo.py mod  -a 10 -b 5        
0
```
https://github.com/nhoyle-unsw/learn-encryption-with-python/blob/main/modulus.py#L12

## Modular multiplicative inverse
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
1. (5 x 3) mod 7 => **15 mod 7** = 1 **Yay!** there is no need to go any further, but lets do it anyway:
1. (6 x 3) mod 7 => **18 mod 7** = 4 
1. (7 x 3) mod 7 => **21 mod **7 = 0
1. (8 x 3) mod 7 => **24 mod 7** = 3
1. (9 x 3) mod 7 => **27 mod 7** = 6
1. (10 x 3) mod 7 => **30 mod 7** = 2
1. (11 x 3) mod 7 => **33 mod 7** = 5
1. (12 x 3) mod 36 => **36 mod 7** = 1 no need to go any further, this just repeats the same pattern, so let's stop.

### Python code example
```
$ python rsa_demo.py modinv -a 3 -m 7      
5
```
https://github.com/nhoyle-unsw/learn-encryption-with-python/blob/main/modulus.py#L29

## References
[1] https://en.wikipedia.org/wiki/Modular_arithmetic