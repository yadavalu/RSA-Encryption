from time import time
from random import randint, choice


def generate_prime( max=101):
    prime = [True for i in range(max + 1)]
    p = 2
    while p ** 2 <= max:
        if prime[p]:
            for i in range(p ** 2, max + 1, p):
                prime[i] = False
        p += 1

    plist = []
    for p in range(max + 1):
        if prime[p]:
            plist.append(p)

    return plist


def generate_random_prime(max=101):
    primes = generate_prime(max)
    return choice(primes)


# 2 factor prime
def prime_factor2(n, iters=None):
    def factor(n):
        g = randint(2, n)
        print(f"Random {g=}")

        while gcd(g, n) != 1:
            print(f"[gcd({g=}, {n=}) != 1, retrying ...]")
            g = randint(2, n)
            print(f"Random {g=}")

        r = 0
        i = 0
        while True:
            i += 1
            print(f"{i=}", end="\r")

            if (g ** i) % n == 1:
                if i % 2 == 0:
                    r = i
                    break
                else:
                    print(f"[Odd power {i=}, retrying ...]")
                    return None

        print(end="")
        print(f"Exponent of g: {r=}")
        g1 = g ** (r / 2) - 1
        # g2 = g ** (r / 2) + 1

        p = gcd(g1, n)
        if p == 1:
            print(f"[gcd({g1=}, {n=}) = 1, retrying ...]")
            return None

        print(f"gcd({g1=}, {n=}) = {p}")
        q = n / p

        return [p, q]

    if iters is None:
        i = 1
        while True:
            p = factor(n)
            if p is not None:
                print()

                return p
            i += 1

    else:
        j = 0
        for i in range(iters):
            p = factor(n)
            if p is not None:
                print()
                print(f"No. of iters = {i + 1}")
                return p
            j = i

        print(f"No. of iters = {j}")
        return None


def gcd(a, b):
    x = max(a, b)
    y = min(a, b)

    while True:
        R = x % y
        if R == 0:
            return y
        x = y
        y = R


if __name__ == '__main__':
    t0 = time()
    # p = prime_factor2(143)
    # p = generate_prime()
    p = generate_random_prime()
    t1 = time()
    dt = t1 - t0
    print(p)
    print(f"{dt=}")
