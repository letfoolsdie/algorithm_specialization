# python3
# -*- coding: utf-8 -*
"""
Created on Thu Sep  8 15:58:33 2016

@author: Nikolay_Semyachkin
"""
def bin_search(arr, hi, lo, key):
    if hi < lo:
        return -1
    mid = int(lo + (hi - lo) / 2)
    if key == arr[mid]:
        return mid
    elif key < arr[mid]:
        return bin_search(arr, mid-1, lo, key)
    else:
        return bin_search(arr, hi, mid+1, key)


#inp1 = '5 1 5 8 12 13'
#inp2 = '5 8 1 23 1 11'
inp1 = input()
inp2 = input()

arr = [int(i) for i in inp1.split()[1:]]
keys = [int(i) for i in inp2.split()[1:]]
hi = len(arr) - 1
lo = 0

for k in keys:
    print(bin_search(arr, hi, lo, k), '', end="")



    
