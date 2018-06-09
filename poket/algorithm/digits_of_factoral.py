from math import log10, pi, e, floor
def DigitsOfFactorial(n):
    if n < 4: return 1
    # Kamenetsky’s formula
    digits = n * log10(n / e) + log10(2 * pi * n) / 2
    return floor(digits) + 1
