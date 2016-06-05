# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 22:19:05 2016

@author: kid
"""
l={0:0,1:1,2:1,3:2,4:2,5:1}

def findway(a,b):
    count=0
    for i in range(len(a)):
        d=a[i]-b
        if d>5:
            count+=d/5
            d=d%5
        
        count+=l[d]
    return count
        
def equal(a):
    m=min(a)
    
    return min(findway(a,m),findway(a,m-1),findway(a,m-2),findway(a,m-3),findway(a,m-4))