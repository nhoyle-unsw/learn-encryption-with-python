## RSA Encryption and Decrption

{% include navigation.html %}

RSA is an acronym made up from the surnames of its inventors [1]: 
- Ronald **R**ivest: 
- Adi **S**hamir:
- Leonard **A**dleman: 

**Ronald Rivest** also invented RC2, 4, 5 and 6 symetric key encryption algorithms as well as the well the MD2, 4, 5 and 6 family of hash functions. https://en.wikipedia.org/wiki/Ron_Rivest [2]

**Adi Shamir** was a co-discoverer of Differential Cryptanalysis: https://en.wikipedia.org/wiki/Differential_cryptanalysis, which was later reveled to have been already known by IBM and the NSA. https://en.wikipedia.org/wiki/Adi_Shamir [3]

**Leonard Adleman** is widely referred to as the Father of DNA Computing, where DNA is used to commpute an algorithm. He is also the co-discoverer fo the  Adleman–Pomerance–Rumely primality test. https://en.wikipedia.org/wiki/Leonard_Adleman [4]

## History
The RSA algortihm was published in in 1977, but again, had an equivalent system that was developed by the British signals intelligence agency (GCHQ) in 1973 [1]

RSA is a public-key encryption system where the encryption key is published for everyone to know and the decryption key is kept secret or private. Two large prime numbers are used to create the public and the private key. The two prime numbers are kept secret also and can be discarded as they are not needed for the encryption and decryption to take place. 

## Security

The security of RSA relies on the fact that it is very hard (in computing time) to find the factors of the product of two large prime numbers.

Distinct from the "factoring problem" mentioned above there is also the "RSA problem" which is about breaking the RSA algorithm by using only the public key. 
For RSA key sizes that are in excess of 1024 bits there is no known efficient method for solving this problem [5]. If ever a method was developed that could solve the RSA problem efficiently then it could threaten current crypto systems or eventual security of systems that used it in the past as a way to encrypt information. 

There have been reports of progress towards cracking RSA encryption using SHor's algorithm and quantum coonpters: https://spectrum.ieee.org/encryptionbusting-quantum-computer-practices-factoring-in-scalable-fiveatom-experiment [6]

## RSA Encryption

Todo

## RSA Decryption

Todo

## Refernces

[1]: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
[2]: https://en.wikipedia.org/wiki/Ron_Rivest
[3]: https://en.wikipedia.org/wiki/Adi_Shamir
[4]: https://en.wikipedia.org/wiki/Leonard_Adleman
[5]: https://en.wikipedia.org/wiki/RSA_problem
[6]: https://spectrum.ieee.org/encryptionbusting-quantum-computer-practices-factoring-in-scalable-fiveatom-experiment
[7]: https://cacr.uwaterloo.ca/hac/


