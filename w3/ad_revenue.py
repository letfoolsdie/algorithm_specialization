# python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 11:58:42 2016

@author: Nikolay
"""

#profit = [1, 3, -5]
#av_clicks = [-2, 4, 1]
#profit = [23]
#av_clicks = [39]
n = int(input())
profit = [int(i) for i in input().split()]
av_clicks = [int(i) for i in input().split()]

profit = sorted(profit)
av_clicks = sorted(av_clicks)
ans = sum([i[0] * i[1] for i in zip(profit, av_clicks)])
print(ans)