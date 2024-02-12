def FME(a, b, c):
    if b > c and gcd(b, c) == 1: b = b % phi(c)
    return _FME(a, b, c)

def _FME(a, b, c):
    if b == 0: return 1
    rem = FME(a, b // 2, c)
    if b % 2: return rem * rem * a % c
    return rem * rem % c

def gcd(a, b):
    while b: a, b = b, a % b
    return a

def phi(n):
    prod = n
    if not n % 2:
        prod -= prod // 2
        while not n % 2:
            n //= 2
    i = 3
    while i * i <= n:
        if not n % i:
            prod -= prod // i
            while not n % i:
                n //= i
        i += 2
    if n != 1:
        prod -= prod // n
    return prod

'''
Fermat's Little Theorem
if p is prime and does not divide a
then a^(p - 1) % p = 1

a^n % p = ?
let m + p - 1 = n
a^(m + p - 1) % p
= [a^m * a^(p - 1)] % p
= (a^m % p) * [a^(p - 1) % p] % p
= (a^m % p) * 1 % p
= a^m % p
= a^[n - (p - 1)] % p

apply that again and again
subtract (p - 1) from the exponent untill we have a remainder
we will have a reduced exponent
so the left exponent simply is n % (p - 1)
thus:

a^n % p = a^[n % (p - 1)] % p

Euler's Theorem: generalized Fermat's Little Theorem
if a and n are relatively prime (or gcd(a, n) = 1)
then a^phi(n) % n = 1
where phi is the Euler's Totient Function
counts n's relatively prime numbers up to n
(for FLT, when n is prime, phi(n) is obviously n - 1)

a^n % m = a^[n % phi(m)] % m

phi(n) = n * PI(1 - 1/p_i), where p_i is a prime factor of n




Fast Exponentiation
a^n = a^(n//2) * a^(n//2) (* a if n is odd)
recursively done
obviously O(log n), better than a*a*a*a*... which is O(n)
(use bit mask to check parity)

when the exponent is too large, there is no point to do this
the answer is so large that we are not able to store it anyway

but it can help with the Modular Exponentiation problem
let's get beck to the Fermat's Little Theorem problem
we found that a^n % p = a^[n % (p - 1)] % p
what if p, the prime itself, is very big?
then n % (p - 1) may be (p - 2) in the worst case
typically the large prime 1 000 000 007 is used in the ICPC

recall a^n = a^(n//2) * a^(n//2) (* a if n is odd)
ignore the parity thing for simplicity here
a^n % c
= a^(n//2) * a^(n//2) % c
= [a^(n//2) % c] * [a^(n//2) % c] % c
recursively done
this % c inside every recursive level keeps the number small
and the whole thing is O(log n)
'''
