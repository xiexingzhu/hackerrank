# -*- coding: utf-8 -*-
"""
Created on Sat Jun 04 14:14:21 2016

@author: kid

hackerrank Algorithms Dynamic Programming The Longest Increasing Subsequence
"""
import bisect
def longestsub(a):
    tail=[a[0]]
    l=1
    
    for i in range(1,len(a)):
        if a[i]>tail[-1]:
            tail.append(a[i])
            l+=1
        elif a[i]<tail[0]:
            tail[0]=a[i]
        elif a[i]==tail[0] or a[i]==tail[-1]:
            continue
        else:
            
            n=bisect.bisect_right(tail,a[i])
            if not a[i]==tail[n-1]:
                tail[n]=a[i]
            
            
    return l
            
    
