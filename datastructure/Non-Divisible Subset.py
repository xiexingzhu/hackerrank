# -*- coding: utf-8 -*-
"""
Created on Sat May 28 21:17:51 2016

@author: kid

hackerrank Week of Code -20  Non-Divisible Subset
"""

from collections import Counter
n,k=map(int,raw_input().strip().split())

a=map(int,raw_input().strip().split())

T0=False
T2=False

if k==1:
    print 0
else:
    c={}
    for i in range(len(a)):
        tmp=a[i]%k
        if not tmp==0 and not tmp*2==k:
            if not tmp in c:
                c[tmp]=1
            else:
                tmp=k-tmp
                for key in c.keys():
                    if not key==tmp:
                        c[key]+=1
        elif tmp==0:
            T0=True
        else:
            T2=True
                        
    count=max(c.values())
    
    if T0 and T2:
        count+=2
    elif T0:
        count+=1
    elif T2:
        count+=1
   
    
    print count
