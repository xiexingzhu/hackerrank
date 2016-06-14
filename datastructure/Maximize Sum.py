# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 13:47:27 2016

@author: kid

hackerrank Algorithms Search Maximize Sum
"""

def maximizesum(a,m):
    a[0]=a[0]%m
    for i in range(1,len(a)):
        a[i]=(a[i]+a[i-1])%m
        
    count=0
    for i in range(1,len(a)):
        for j in range(i-1,-1,-1):
            if a[j]>a[i]:
                count=max(count,((a[i]-a[j])+m)%m)
        count=max(count,a[i])
        
    print count
                
                
                
        

