#!/usr/bin/env python3
from math import sqrt


def primes():
    prime = 1
    while True:
        prime += 2
        if all(prime % i for i in range(2, int(sqrt(prime)+1))):
            yield prime


total = 2
for i in primes():
    print(i)
    if i > 2000000:
        break
    total += i

print("total: {}".format(total))
