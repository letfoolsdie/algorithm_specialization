# python3
# -*- coding: utf-8 -*
"""
Created on Thu Sep  8 15:58:33 2016

@author: Nikolay_Semyachkin
"""

#inp1 = '5 1 5 8 12 13'
#inp2 = '5 8 1 23 1 11'
inp1 = input()
inp2 = input()

arr = [int(i) for i in inp1.split()[1:]]
keys = [int(i) for i in inp2.split()[1:]]

#for k in keys:
#    if k in arr:
#        print(arr.index(k), '', end="")
#    else:
#        print(-1, '', end="")

# well, that didn't work