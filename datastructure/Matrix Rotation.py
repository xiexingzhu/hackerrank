# -*- coding: utf-8 -*-
"""
Created on Tue May 24 21:21:15 2016

@author: xy
"""
# this to solve hackerrank problem Matrix Rotation
# which is not an easy one to me now

def rotate(a,r):
    for i in range(len(a)):
        a[i]=a[i].rotate(r)
        
def changelist(a):
    new=[]
    
    for i in range(len(a)):
        if i==0:
            new.append(a[i])
        elif i==len(a)-1:
            


