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

# Pe = event probability
# let X be the number of times the event happens
# returns the probability of X is in [lower, upper)
def P_range(Pe, trial, lower = 0, upper = 0):
    if not upper:
        upper = trial + 1
    _Pe, Pr = 1.0 - Pe, 0.0
    for i in range(lower, upper):
        Pr += Pe**i * _Pe**(trial - i) * C(trial, i)
    return Pr
