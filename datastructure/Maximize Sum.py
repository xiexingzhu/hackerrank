# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 13:47:27 2016

@author: kid

hackerrank Algorithms Search Maximize Sum
"""

T = int(raw_input())
for t in range(T):
    [N, M] = [int(x) for x in raw_input().split()]
    array = [int(x) for x in raw_input().split()]
    prefix_sum = [array[0] % M]
    for i in range(1, N):
        prefix_sum.append((prefix_sum[i - 1] + array[i]) % M)
    bi_sum = [(prefix_sum[i], i) for i in range(N)]
    bi_sum.sort()
    mmod = bi_sum[-1][0]
    for i in range(1, N):
        if bi_sum[i][1] < bi_sum[i-1][1] and M - (bi_sum[i][0] - bi_sum[i-1][0]) > mmod:
            mmod = M - (bi_sum[i][0] - bi_sum[i-1][0])
    print mmod
                
                
                
        

