# python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:44:54 2016

@author: Nikolay_Semyachkin
"""

m = 10
inp = [int(i) for i in input().split()]
n1 = inp[0] - 1
n2 = inp[1]


def F():
    yield 0
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

def pisano(m):        
    period = []#[0, 1]
    fib = F()
    while True:
        period.append(next(fib) % m)
        if (period[-1] == 1) and (period[-2] == 0) and len(period) > 2:
            break
    return period[:-2]


def find_sum(n, pis):
    ind = (n+2) % len(pis)
    ans = pis[ind]
    if ans == 0:
        return 9
    else:
        return ans - 1
    
pis = pisano(m)
ans1 = find_sum(n1, pis)
ans2 = find_sum(n2, pis)
#print(find_sum(n, pis))
nums = [i for i in range(10)]
print(nums[ans2-ans1])
#ind = (n+2) % len(pis)
#ans = pis[ind]
#if ans == 0:
#    print(9)
#else:
#    print(ans - 1)
