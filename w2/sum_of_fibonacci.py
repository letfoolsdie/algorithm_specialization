# Uses python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 10:15:09 2016

@author: Nikolay_Semyachkin
"""
m = 10
n = int(input())
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
    
pis = pisano(m)

#k = 100 
#total = 0
#x = F()
#for _ in range(k+2):
#    total = next(x)
##    print(total)
#print(total - 1)    
ind = (n+2) % len(pis)
ans = pis[ind]
if ans == 0:
    print(9)
else:
    print(ans - 1)
#if ind <= 1:
#    print(pis[ind])
#else:
#    print(pis[ind])
