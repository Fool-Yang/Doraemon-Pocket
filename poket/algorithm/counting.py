class Counting:

    def P(n, k):
        return Product(n - k + 1, n)

    def C(n, k):
        if n - k > k:
            k = n - k
        return Product(k + 1, n) // Product(1, n - k)

    def Product(a, b):
        pro = 1
        for i in range(a, b + 1):
            pro *= i
        return pro

    def P_range(Pe, trial, lower = 0, upper = 0):
        if not upper:
            upper = trial + 1
        Pe_, Pr = 1.0 - Pe, 0.0
        for i in range(lower, upper):
            Pr += Pe ** i * Pe_ ** (trial - i) * C(trial, i)
        return Pr
