#!/usr/bin/env python3
def gen():
    num = 1
    while True:
        num += 2
        if all( num % i != 0 for i in range(2,num)):
            yield num
        #yield num

prime = 0
g = gen()
for i in range(1,6):
    prime = next(g)
    print(prime, i)
print(prime)
