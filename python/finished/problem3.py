#!/usr/bin/env python3

def is_prime(n):
    if n < 2:
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
    return True

x = 2
big_num = 600851475143
while big_num > 1:
    if is_prime(x):
        if big_num % x == 0:
            big_num /= x
    x+=1
print(x)
