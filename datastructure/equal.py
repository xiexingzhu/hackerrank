# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 16:01:31 2016

@author: kid

hackerrank Algorithms Dynamic Programming  Equal
"""

l={0:0,1:1,2:1,3:2,4:2,5:1}

def equal(a,m,n):
    if n-m==1:
        if a[m]==a[n]:
            return 0
        else:
            count =a[n]-a[m]
            Count=count/5
            count=count%5
            
            return l[count]+Count
        
        
    else:
        count=a[n]-a[m]
        tmp=equal(a,m,n-1)
        Count=count/5
        count=count%5
        tmp+=Count
        #print count
        tmp+=l[count]
            
        return tmp
            
            
            
