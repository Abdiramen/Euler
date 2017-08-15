#!/usr/bin/env python3
string = ''
with open('big_num') as f:
    for line in f:
        string = string + line.rstrip('\n')
        #print(string)

product = 0
lst = []
for i in range(0,len(string)):
    mult = 1
    temp = []
    for j in string[i : i + 13]: # change 4 to 13 in final version
        mult *= int(j)
        temp.append(int(j))
    if mult > product:
        product = mult
        lst = temp
print(product)
print(lst)
