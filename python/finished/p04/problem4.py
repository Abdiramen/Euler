#!/usr/bin/env python3

largest = 0
for i in range(100,999):
    for x in range(i,999):
        string = str(i*x)
        if string == string[::-1] and i*x > largest:
#            print(i*x)
            largest = i*x
print(largest)
