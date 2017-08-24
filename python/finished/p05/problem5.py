#!/usr/bin/env python3


def factor(num, primes):
    factors = []
    for i in primes:
        while num % i == 0:
            factors.append(i)
            num //= i
            if num == 1:
                break
    return factors


if __name__ == "__main__":
    n = int(input("n = "))
    primes = [ p for p in range(2,n+1) if all( p % x != 0 for x in range( 2, p ) ) ]
    powers = [ 1 for p in primes ]
    mult = 1
    for p in primes:
        mult*=p
    composites = [ c for c in range(2,n+1) if c not in primes ]
    for p in primes:
        for c in composites:
            factors = factor(c,primes)
            count = 0
            for f in factors:
                    if f == p:
                        count += 1
                        if count > powers[primes.index(p)]:
                                powers[primes.index(p)] = count
    print('primes ', primes)
    print('powers ', powers)
    print('composites ', composites)
    mult = 1
    for p in primes:
        mult *= p**powers[primes.index(p)]
    print('solution ', mult)
