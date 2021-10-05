## Conversion of text to numbers and blocks

{% include navigation.html %}

## Problems with RSA

**Problem 1**. RSA uses the properties of modular arithmetic and prime numbers in order to provide a really neat way of implementing asymmetric encryption. One problem is that it can only be used to encrypt numbers. So, so we need to find a way to convert our plaintext message into a number so we can encrypt it.

**Problem 2**. Another thing to notice is that RSA can only encrypt a number up to the size of the modulus n (see <a href="rsa">RSA Encryption and Decryption</a>). This mens you will need to have very large prime numbers if you want to encrypt a large amount of plaintext. So we also need a way to break up a message into smaller chunks and process them separately. **Please note** that using RSA in this way have some security concerns (see Security notes in <a href="rsa">RSA Encryption and Decryption</a> ), another reason why not to roll your own encryption.

## Conversion of text to numbers

There are many decisions to be made when you want to convert text to numbers:

- Which characters will you support in your alphabet?
- How many characters are in your alphabet and how many numbers do you need to represent each character?
- Can you transform back to the characters without loss or is some loss like capitalisation acceptable?

## Breaking text up into blocks

Similar to the text <--> numbers conversion issues above we need to ask ourselves some questions when we want to break our plaintext up into blocks:

- What is the maximum number that we can encrypt without going above the size of the modulus n (the product of the two primes)
- Another way of looking at it is: if i choose a block size, what is the minimum size of prime numbers i need to use so I can encode for that. For example if you use 3 numbers per character and want to encode 10 characters per block, then your n will need to be at least 30 digits long. This means you prime numbers need to be at least 15 digits long each. 1 x 10 ^ 15 . 1 x 10 ^ 15 = 1 x 10 ^ 30
- What if your text starts with the biggest numbered character?
- How do you make as many characters fit into as few numbers as possible?

These questions will be addressed below to show you how I have selected answers to these questions ans some justifications. In general, I have selected for simplicity over efficiency. This is for demonstration purposes only and should never be used in any other context.

For my block algorithm I chose:

- Use ASCII[^ascii] character set for numbering
  -- Justification: ASCII covers all of the western alphabet and numbers plus many of the standard punctuation and symbols used in every day conversations. This is sufficient for demonstration purposes. It could be extended to include unicode to cover international characters and "control" characters.
- Alphabet: I chose to include all the control characters (from ascii 0) and the printable characters up to and including the character at ascii 155. Why? I wanted to make it clear and easy to understand.
- Leading zeros on a number will be lost because they are meaningless to mathematics. So my character range is from ascii 0 - 155 (Null... control characters, symbols, 0-9, symbols, A-Z, symbols, a-z, symbols, up to '>' which is at ascii 155). I add 100 on to the ascii code for each so that I have no leading zeros. So , my range is now 100 - 255. This could potentially be stored as 8 bits for each character rather than just as plain characters, but again for clarity I chose not to do that.

The converter functions are used to both translate the text to and from numbers and also to break it up into manageable chunks of 10 characters each (or 30 numbers). Padding is also added so that each block is exactly 30 numbers. These are stripped out when the decryption and de-translation happens:
**Source code:** [Source code at GitHub](https://github.com/nhoyle-unsw/learn-encryption-with-python/blob/main/converter.py)

## References

[^1]: <https://stackoverflow.com/questions/4528982/convert-alphabet-letters-to-number-in-python>
[^ascii]: <https://www.ascii-code.com/>
[^max-rsa-size]: <https://info.townsendsecurity.com/bid/29195/how-much-data-can-you-encrypt-with-rsa-keys>
[^string-to-integer]: <https://www.geeksforgeeks.org/convert-string-to-integer-in-python/>
[^iterate-over-nth-character]: <https://stackoverflow.com/questions/51121911/iterate-over-every-nth-element-in-string-in-loop-python>
[^split-string-nth-character]: <https://stackoverflow.com/questions/9475241/split-string-every-nth-character>
[^ascii-value-of-char]: <https://stackoverflow.com/questions/227459/how-to-get-the-ascii-value-of-a-character>
