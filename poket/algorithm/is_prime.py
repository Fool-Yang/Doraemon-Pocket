def IsPrime(n):
    if n < 5:
        return n == 2 or n == 3
    if not (n % 6 == 1 or n % 6 == 5):
        return False
    for m in range(5, int(n ** 0.5) + 1, 6):
        if not (n % m and n % (m + 2)):
            return False
    return True
