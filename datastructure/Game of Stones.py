# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 13:17:11 2016

@author: kid

hackerrank Algorithms Game Theory Game of Stones
"""

def game(n,t):
    if n==1 or n==0:
        if t==1:
            return False
        else:
            return True
            
    elif n>=5:
        if t==1:
            return any([game(n-2,-1),game(n-3,-1),game(n-5,-1)])
        else:
            return all([game(n-2,1),game(n-3,1),game(n-5,1)])
    elif n>=3:
        if t==1:
            return any([game(n-2,-1),game(n-3,-1)])
        else:
            return all([game(n-2,1),game(n-3,1)])
    else:
        if t==1:
            return game(n-2,-1)
        else:
            return game(n-2,1)

