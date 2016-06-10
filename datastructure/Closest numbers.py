# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 20:04:47 2016

@author: kid

hackerrank Algorithms Sorting Closest Numbers
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
        
def quick_sort(ar,p,r):
    if p<r:
        pivot = partition(ar, p, r)
        quick_sort(ar, p, pivot-1)
        quick_sort(ar, pivot+1, r)
        
    return ''

def closest(ar):
    count=abs(ar[1]-ar[0])
    tmp=[]
    for i in range(1,len(ar)):
        if abs(ar[i]-ar[i-1])==count:
            tmp.append(ar[i-1])
            tmp.append(ar[i])
        elif abs(ar[i]-ar[i-1])<count:
            count=abs(ar[i]-ar[i-1])
            tmp=[ar[i-1],ar[i]]
            
    for i in tmp:
        print i,
        
    return ''

a=input()
b=map(int,raw_input().strip().split())
quick_sort(b,0,len(b)-1)
#print b

closest(b)