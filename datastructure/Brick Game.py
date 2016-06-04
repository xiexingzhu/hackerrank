# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 22:02:03 2016

@author: kid

hackerrank Algorithms Dynamic Programming Bricks Game
"""

def brickgame(a,m,n,b):
    if n-m==2:
        if b==1:
            return a[m]+a[m+1]+a[n]
        else:
            return 0
    elif n-m==1:
        if b==1:
            return a[m]+a[n]
        else:
            return 0
    elif n==m:
        if b==1:
            return a[m]
        else:
            return 0
    else:
        if b==1:
            return max(a[m]+brickgame(a,m+1,n,-1),a[m]+a[m+1]+brickgame(a,m+2,n,-1),a[m]+a[m+1]+a[m+2]+brickgame(a,m+3,n,-1))
        else:
            return min(brickgame(a,m+1,n,1),brickgame(a,m+2,n,1),brickgame(a,m+3,n,1))
