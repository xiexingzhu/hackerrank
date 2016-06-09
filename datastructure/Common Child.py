# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 13:26:12 2016

@author: kid

hackerrank Algorithms Strings Common Child
"""

def commonchild(a,b,a1,b1):
    if a1==0 or b1==0:
        if len(set(a[:a1+1]).intersection(set(b[:b1+1])))==1:
            return 1
        else:
            return 0
    else:
        if a[a1]==b[b1]:
            return commonchild(a,b,a1-1,b1-1)+1
        else:
            return max(commonchild(a,b,a1-1,b1),commonchild(a,b,a1,b1-1))
            
            
        

