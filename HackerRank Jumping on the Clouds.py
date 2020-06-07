#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

res = 0
i = 0
while i < n-1:
    if i+2<n and c[i+2] == 0:
        i = i+2
        res += 1
    else:
        i = i+1
        res += 1
print(res)
