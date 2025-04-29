def comb(n, k, mod):

    fact = [0] * (n + 1)
    inv = [0] * (n + 1)
    finv = [0] * (n + 1)

    fact[0], fact[1] = 1, 1
    inv[1] = 1
    finv[0], finv[1] = 1, 1

    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % mod
        inv[i] = mod - ((inv[mod % i] * (mod // i)) % mod)
        finv[i] = (finv[i - 1] * inv[i]) % mod

    return (fact[n] * finv[k] * finv[n-k]) % mod