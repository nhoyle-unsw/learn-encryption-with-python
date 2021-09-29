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

## Relation to regular arithmetic
Modular arithmetic is similar to regular arithmetic for addition, subtraction and multiplication, but not for division [3]. So let's review regular arithmetic as a refresher and then see how it differs. When you multiply the two sides of an equation by the same number it keeps the two sides equal. An example is: 

4x = 16  (lets call this **equation 1**)
so we can work out what x is by putting a number in for x and seeing which one works:
|   x   |   4x   | does this equal 16? |
--------|--------|--------
|   1   |    4   | not 16 |
|   2   |    8   | not 16 |
|   3   |   12   | not 16 |
|   4   | 16     | **= 16 ! Yay!** |

So the x that makes this equation correct is x = 4 because it makes both of the sides equal to 16.

Now, if we start from the same equation again:
4x = 16

But now, let's do something to both sides of the equation. Let's divide each side by 4:
4x/4 = 16/4
x = 4

OK, that seemed to work, let's start again:
4x = 16

And this time, let's try to subtract 8 from both sides:
4x - 8 = 16 - 8
4x - 8 = 8

Now lets divide both sides by 4:
(4x - 8) ÷ 4 = 8 ÷ 4
(4x ÷ 4) - (8 ÷ 4) = 8 ÷ 4
x - 2 = 2
and finally add 2 to both sides
x - 2 + 2 = 2 + 2
and again we end up with:
x = 4

All of these equations are equivalent to the original "equation 1" because x is still equal to 4 even though we multiply and add to both sides by 2. You haven't unbalanced anything because you did the same thing to both sides. This is simple enough to understand for basic arithmetic like addition and multiplication. But for modular arithmetic, it is a little harder to find an equivalent thing we can do to both sides of the equation and still have them balanced with each other. So, let's look at the equivalent in modular arithmetic.

I'll use an example equation **10 mod 7**. We know that the answer to 10 mod 7 is 3 because if we divide 10 by 7 it goes once and we have a remainder of 3. We also know that **3 mod 7** also equals 3 because if we divide 3 by 7 we get zero with a remainder of 3.
So now we can write that 10 mod 7 is equivalent to 3 mod 7. Or in mathematical language, we can say they are congruent. This means both 10 and 3 have the same remainder when divided by 7:
10 ÷ 7 = 1 r **3**
and
3 ÷ 7  = 0 r **3**
We can also write that
**10 mod 7 = 3**
and
**3 mod 7 = 3**

To be precise we don't say they are equal, we say they are "congruent". We can indicate that they are congruent like this:

10 mod 7 ≅ 3 mod 7

Now, what if I wanted to multiply both sides of this equation by a number but still have them congruent with each other, how do I find that number? Let's try 2 and see what happens:

10 X 2 mod 7 ==> 20 mod 7 = 6
3 x 2  mod 7 ==> 6  mod 7 = 6

That looks like it worked, let's try another number. Let's try multiplying by 3:

10 x 3 mod 7 ==> 30 mod 7 = 2
3 x 3  mod 7 ==> 9  mod 7 = 2
That looks like it worked, but I am not sure, it may have been luck, so let's try multiplying by 3 again:

30 x 3 mod 7 ==> 90 mod 7 = 6
9 x 3  mod 7 ==> 27  mod 7 = 6

So it appears you can multiply both sides by the same number and have them still be congruent. This also works for addition and subtraction. In fact, the following all hold true for modular arithmetic:

>  Sometimes the calculation can be simplified because for any integer a1, b1, a2 andb2, if we know that a1 ≡ b1 mod n and a2 ≡ b2 mod n then the following always holds:  
>  a1+a2 ≡ b1+b2 mod n  
>  a1-a2 ≡ b1-b2 mod n  
>  a1*a2 ≡ b1*b2 mod n  
>
[3]

Division is another story though. So, can we do division at all? The answer is, sometimes we can and sometimes we can't [3]. It is not always possible to divide using modulo arithmetic because zero appears quite often. We all remember that division by zero is not defined. Also, we are operating in whole numbers and cannot have results that are fractions. So what can we do? How can we work out when it is OK to divide modular equations? What is the inverse of multiplication? 
 
## Modular multiplicative inverse
The modular multiplicative inverse is asking the following question:
If I have a number **a** and I want to divide it by **m** and get a remainder of 1, so what would I need to multiply **a** by to get a remainder of 1? 

In maths symbols, it looks like this:
Solve this by finding an x that satisfies: a**x** = 1 (mod m)

If we can find this magic x then we will be able to use it to divide our equations. 

You can find this x by trial and error. So let's try 0a mod m, then 1a mod m, then 2a mod m, then 3a mod m, until you get an answer of 1. Here is an example:
Find the mod inverse of 3 mod 7 = 3. To do this we need to find an x that gives us an answer of 1 for 3x mod 7, or:
3x ≅ 1 (mod 7)
Let's start at 1 and work our way up (there is no point starting a zero because "0 mod n" is zero for all numbers)
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
1. (12 x 3) mod 7 => **36 mod 7** = **1** **Yay!** no need to go any further, this just repeats the same pattern, so let's do one more:
1. (13 x 3) mod 7 => **39 mod 7** = 4 
1. (14 x 3) mod 7 => **42 mod 7** = 0
1. (15 x 3) mod 7 => **45 mod 7** = 3
1. (16 x 3) mod 7 => **48 mod 7** = 6
1. (17 x 3) mod 7 => **51 mod 7** = 2
1. (18 x 3) mod 7 => **54 mod 7** = 5
1. (19 x 3) mod 7 => **57 mod 7** = **1** **Yay!** no need to go any further. Let's stop here.
(see [2]). It is not surprising that we see this repeating every 7th iteration as we are using modulo 7.

### Python code example (the long way)
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

## More formal definition
The example definition above was in order to show a simple algorithm for calculating the multiplicative modular inverse. A more formal definition can be stated as follows:

> The modular multiplicative inverse is an integer **x** such that:  
>  
> a x ≅ 1 (mod m)  
>  
> The value of x should be in the range { 1, 2, … m-1}, i.e., in the range of integer modulo m.  
> (Note that: x cannot be 0 as 0 mod m = 0 for all m and will never be 1)  
> The multiplicative inverse of “a modulo m” exists if and only if a and m are relatively prime (i.e. if gcd(a, m) = 1).  
>
[2]

### Python code example (the short way)
```sh
$ python rsa_demo.py modinv -a 3 -m 7       
5
```
**Source code:** https://github.com/nhoyle-unsw/learn-encryption-with-python/blob/main/modulus.py#L29

```sh
$ python rsa_demo.py modinv_euclid -a 3 -m 7 
5
```
**Source code:** https://github.com/nhoyle-unsw/learn-encryption-with-python/blob/main/modulus.py#L55

## References
[1] https://en.wikipedia.org/wiki/Modular_arithmetic  
[2] https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/  
[3] http://www.doc.ic.ac.uk/~mrh/330tutor/ch03.html  