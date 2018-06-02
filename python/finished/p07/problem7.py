#!/usr/bin/env python3
from math import sqrt


def primes():
    prime = 1
    count = 1
    while True:
        prime += 2
        if all(prime % i for i in range(2, int(sqrt(prime)+1))):
            count += 1
            yield count, prime
        if count == 10001:
            return prime


for p in primes():
    print(p)
