## RSA Encryption and Decryption

{% include navigation.html %}

RSA is an acronym made up from the surnames of its inventors [^1]:

- Ronald **R**ivest:
- Adi **S**hamir:
- Leonard **A**dleman:

**Ronald Rivest** also invented RC2, 4, 5 and 6 symmetric key encryption algorithms as well as the well the MD2, 4, 5 and 6 family of hash functions. https://en.wikipedia.org/wiki/Ron_Rivest [^2]

**Adi Shamir** was a co-discoverer of Differential Cryptanalysis: https://en.wikipedia.org/wiki/Differential_cryptanalysis, which was later reveled to have been already known by IBM and the NSA. https://en.wikipedia.org/wiki/Adi_Shamir [^3]

**Leonard Adleman** is widely referred to as the Father of DNA Computing, where DNA is used to compute an algorithm. He is also the co-discoverer fo the Adleman–Pomerance–Rumely primality test. https://en.wikipedia.org/wiki/Leonard_Adleman [^4]

## History

The RSA algorithm was published in in 1977, but again, had an equivalent system that was developed by the British signals intelligence agency (GCHQ) in 1973 [^1]

RSA is a public-key encryption system where the encryption key is published for everyone to know and the decryption key is kept secret or private. Two large prime numbers are used to create the public and the private key. The two prime numbers are kept secret also and can be discarded as they are not needed for the encryption and decryption to take place.

## Security

The security of RSA relies on the fact that it is very hard (in computing time) to find the factors of the product of two large prime numbers, this is known as the "factoring problem" [^1].

Distinct from the "factoring problem" mentioned above there is also the "RSA problem" which is about breaking the RSA algorithm by using only the public key.
For RSA key sizes that are in excess of 1024 bits there is no known efficient method for solving this problem [^5]. If ever a method was developed that could solve the RSA problem efficiently then it could threaten current crypto systems or eventual security of systems that used it in the past as a way to encrypt information.

There have been reports of progress towards cracking RSA encryption using Shor's algorithm and quantum computers as seen in https://spectrum.ieee.org/encryptionbusting-quantum-computer-practices-factoring-in-scalable-fiveatom-experiment, but this has only been done for the number 15 [^6]. However, it appears that this factorisation of 15 into 3 x 5 may be classified informally as one of the "stunt" factorisations where experiments are set up knowing the factors already, which is not a valid test of an algorithm that is supposed to be finding unknown factors. So it seems a long way off at the moment.

## RSA Key generation

Alice can create an RSA public key and private key using the following method (with example on the right)

| Step | Procedure&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                                                                                                                                       | Example&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Comment&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                                          |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 1    | Generate two prime numbers **_p_** and **_q_** that are different to each other, but around about the same size, but not too close to each other (see Security Notes).                                                  | p = 557 q = 839                                                                 | both prime numbers                                                                                                       |
| 2    | Calculate **_n_** = **_p_** x **_q_** - this will be used as the modulus                                                                                                                                                | n = p \* q = 467323                                                             | n is part of the public key                                                                                              |
| 3    | Calculate the totient of the primes **_m_** = φ(**_n_**) = φ(**_p_**).φ(**_q_**) = (**_p_**-1).(**_q_**-1)                                                                                                              | m = (p-1) \* (q-1) = 465928                                                     | m is used to calculate the decryption key                                                                                |
| 4    | Choose your encryption key **_e_** : which needs to be larger that 1 and less than **_m_**. Also **_e_** and **_m_** should be coprime. So their greatest common denominator should be 1. Or gcd(**_e_**, **_m_**) = 1. | e = 7825                                                                        | e is co-prime with m                                                                                                     |
| 5    | Calculate the decryption key **_d_**. We do this by finding the modular multiplicative inverse for **_e_** in this equation: **_e_**.**_d_** ≅ 1 (mod **_m_**).                                                         | 7825 . d ≅ 1 (mod 465928)                                                       | inverse of 7825 mod 465928 https://www.wolframalpha.com/input/?i=inverse+of+7825+mod+465928                              |
| 6    | The private key is **_d_**                                                                                                                                                                                              | d = 214833                                                                      | Alice uses d and n to decrypt a message from anyone                                                                      |
| 7    | The public key is both **_n_** and **_e_**                                                                                                                                                                              | n = 467323 e = 7825                                                             | Alice published the encryption key e and the number n as the public key. Anyone can encrypt messages for her to decrypt. |
| 8    | Throw away the other numbers, you don't need them.                                                                                                                                                                      |                                                                                 | Alice no longer needs p, q or m. So, she discards them safely.                                                           |

## RSA Encryption - Bob using public key to encrypt

1. Bob has a message "Hello Alice" to encrypt and send to Alice
1. Convert the message to a number: convert

## RSA Decryption - Alice using private key to decrypt

Todo

## Security notes

1. In practice these two elected prime numbers should be large and randomly selected. There other considerations to make the possibility of attacks less likely. This is one reason why you should never implement your own encryption as the mathematics behind it is very complex.

## References

[^1]: <https://en.wikipedia.org/wiki/RSA_(cryptosystem)>
[^2]: <https://en.wikipedia.org/wiki/Ron_Rivest>
[^3]: <https://en.wikipedia.org/wiki/Adi_Shamir>
[^4]: <https://en.wikipedia.org/wiki/Leonard_Adleman>
[^5]: <https://en.wikipedia.org/wiki/RSA_problem>
[^6]: <https://spectrum.ieee.org/encryptionbusting-quantum-computer-practices-factoring-in-scalable-fiveatom-experiment>
[^7]: <https://cacr.uwaterloo.ca/hac/>
[^8]: <https://cacr.uwaterloo.ca/hac/about/chap8.pdf>
[^9]: <https://stackoverflow.com/questions/4528982/convert-alphabet-letters-to-number-in-python>
