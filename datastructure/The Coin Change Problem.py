# -*- coding: utf-8 -*-
"""
Created on Tue May 31 15:01:20 2016

@author: kid

hackerrank Algorithms Dynamic Programming The Coin Change Problem
"""


def Coinchange(n,m):
    if n==0:
        return 1
    elif len(m)==1:
        if n%m[0]==0:
            return 1
        else:
            return 0
    else:
        tmp=0
        while(n>=0):
            tmp+=Coinchange(n,m[1:])
            n-=m[0]
        return tmp
            
        