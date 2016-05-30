# -*- coding: utf-8 -*-
"""
Created on Sat May 28 21:17:51 2016

@author: kid

hackerrank Week of Code -20  Non-Divisible Subset
"""

from collections import Counter
n,k=map(int,raw_input().strip().split())

a=map(int,raw_input().strip().split())

if k==1:
    print 1
else:
    for i in range(len(a)):
        a[i]=a[i]%k
    tmp=Counter(a)
    count=0
    
    if k%2==0:
        if k/2 in tmp:
            count+=1
        for i in range(1,k/2):
            if i in tmp and k-i in tmp:
                count+=max(tmp[i],tmp[k-i])
            elif i in tmp:
                count+=tmp[i]
            elif k-i in tmp:
                count+=tmp[k-i]
        if 0 in tmp:
            count+=1
        print count
    else:
        for i in range(1,k/2+1):
            if i in tmp and k-i in tmp:
                count+=max(tmp[i],tmp[k-i])
            elif i in tmp:
                count+=tmp[i]
            elif k-i in tmp:
                count+=tmp[k-i]
        if 0 in tmp:
            count+=1
        print count