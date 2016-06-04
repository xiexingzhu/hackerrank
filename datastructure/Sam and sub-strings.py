# -*- coding: utf-8 -*-
"""
Created on Sat Jun 04 13:09:15 2016

@author: kid

hackerrank Algorithms Dynamic Programming Sam and sub-strings
"""

def sam(a):
    Count=int(a[0])
    count=int(a[0])
    
    for n in range(1,len(a)):
        count=count*10+int(a[n])*(n+1)
        Count+=count
        
    return Count

print sam(raw_input())%(10**9+7)


            
