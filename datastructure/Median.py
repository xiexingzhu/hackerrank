# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 20:13:05 2016

@author: kid

hackerrank Algorithms Sorting Find the Median
"""
def partition(ar,p,r):
    key = ar[r]
    i = p-1
    for j in xrange(p,r):
        if ar[j]<=key:
            i=i+1
            ar[i],ar[j]=ar[j],ar[i]
    ar[i+1],ar[r]=ar[r],ar[i+1]
    return i+1
    
def median(ar,p,r,n):
    t=partition(ar,p,r)
    
    if t==n:
        print ar[t]
        #return ''
    elif t>n:
        median(ar,p,t-1,n)
    else:
        median(ar,t+1,r,n)
        
    #return ''

#a=input()
#b=map(int,raw_input().strip().split())

#print median(b,0,len(b)-1,(len(b)-1)/2)
