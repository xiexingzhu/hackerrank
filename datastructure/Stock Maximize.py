# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 21:44:03 2016

@author: kid

hackerrank Algorithms Dynamic Programming Stock Maximize
"""

def Stockmaximize(a):
    tmp=[[a[0],0]]
    count=0
    
    for i in range(len(a)):
        count+=a[i]
        while(len(tmp)>0):
            if a[i]>tmp[-1][0]:
                tmp.pop()
            else:
                break
        tmp.append([a[i],i])

    Count=0        
    t=-1
    for i in range(len(tmp)):
        Count+=tmp[i][0]*(tmp[i][1]-t)
        t=tmp[i][1]
        
    return Count-count
        