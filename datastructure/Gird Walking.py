# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 09:58:09 2016

@author: kid

hackerrank Algorithms Dynamic Programming Grid Walking
"""

def Gridwalking(I,s,d,item):
    if s==0:
        if I==item:
            return 1
        else:
            return 0
    else:
        t=[]
        for i in range(len(item)):
            #print item
            if item[i]-1>0:
                tmp=item[:]
                tmp[i]-=1
                t.append(Gridwalking(I,s-1,d,tmp))
            if item[i]+1<=d[i]:
                tmp=item[:]
                tmp[i]+=1
                t.append(Gridwalking(I,s-1,d,tmp))
    return sum(t)
        
    
