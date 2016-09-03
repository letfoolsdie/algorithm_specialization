# python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 12:17:51 2016

@author: Nikolay
"""
n = int(input())
nums = [i for i in input().split()]

def compare(n, m):
    if n+m > m+n:
        return n
    else:
        return m
    
ans = ''

while nums:
    max_digit = ' '
    for n in nums:
        max_digit = compare(max_digit, n)
    ans += nums.pop(nums.index(max_digit))

print(ans)

    