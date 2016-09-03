# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 23:18:43 2016

@author: Nikolay
"""
n = 65
def F():
    yield 0
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a
        
x = F()
#ans = 0
#for i in range(n+1):
#    ans += next(x)
#    print(ans%10)
##print(ans%10)