# python3
# BEWARE: this is wrong solution. I couldn't make it to pass all cases.
# if you can find a mistake, contact me, I'll buy you a beer :)
# for correct solution see another file cop_frac_knapsack.py
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 10:07:25 2016

@author: Nikolay
"""
cap = 40
collected_value = 0
vals = [10, 15, 120]
whts = [20, 1.33 , 40]
#vals = [60, 100, 120]
#whts = [20, 50, 30]
#vals = [500]
#whts = [30]

#import sys
#data = list(map(int, sys.stdin.read().split()))
#n, cap = data[0:2]
#vals = data[2:(2 * n + 2):2]
#whts = data[3:(2 * n + 2):2]
#collected_value = 0

frac_vals = [i[0] / i[1] for i in zip(vals, whts)]

while (len(frac_vals) > 0) and (cap > 0):
    put_item = frac_vals.index(max(frac_vals))
    if whts[put_item] <= cap:
        collected_value += vals[put_item]
        cap -= whts[put_item]
        del frac_vals[put_item]
        del vals[put_item]
        del whts[put_item]
    else:
        can_take = cap#whts[put_item] - cap
        collected_value += vals[put_item] * (can_take / whts[put_item])
        cap -= can_take
        del frac_vals[put_item]
        del vals[put_item]
        del whts[put_item]

#print(collected_value)
print("{:.10f}".format(collected_value))