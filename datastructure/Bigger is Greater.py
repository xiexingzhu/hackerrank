# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 21:05:57 2016

@author: kid

hackerrank Algorithms Sorting Bigger is Greater
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

def bigerisgreater(a):
    A=list(a)
    m=-1
    
    for i in range(len(A)-1,0,-1):
        if m==-1:
            j=i
            while(j>=0):
                if A[i]>A[j]:
                    m=j
                    t=False
                    A[i],A[j]=A[j],A[i]
                    break
                j-=1
        
    if m==-1:
        return 'no answer'
    else:
        quick_sort(A,m+1,len(A)-1)
        #print ''.join(A)
    return ''.join(A)
    

