# -*- coding: utf-8 -*-
"""
Created on Tue May 24 21:21:15 2016

@author: xy
"""
# this to solve hackerrank problem Matrix Rotation
# which is not an easy one to me now

import math
from collections import deque

def rotate(a,r):
    for i in range(len(a)):
        a[i].rotate(-r)
        
def matrixchange(a):
    a=deque([deque(i) for i in a])
    tmp=[]
    
    while(sum([0 if i==deque([]) else 1 for i in a])>1):
        new=[]
        new.extend(list(a.popleft()))
        for i in range(len(a)):
            new.append(a[i].pop())
        new.extend(list(a.pop())[::-1])
        if len(a)>0:
            for i in range(len(a)-1,-1,-1):
                new.append(a[i].popleft())
        tmp.append(new)

    if not sum([0 if i==deque([]) else 1 for i in a])==0:
        tmp.append(list(a[0]))
        
    return deque([deque(i) for i in tmp])
        
        
def showmatrix(a,n,m):
    b=deque(a)
    if n%2==0:
        nn=n/2-1
    else:
        nn=n/2
    for i in range(n):
        if i>nn:
            i=n-i-1
        
            j=0
            while(j<i):
                print b[j].pop(),
                j+=1
            for _ in range(m-2*i):
                print b[i].pop(),
        
            if i>0:
                j=i-1
                while(j>-1):
                    print b[j].popleft(),
                    j-=1
            
        else:
            j=0
            while(j<i):
                print b[j].pop(),
                j+=1
            for _ in range(m-2*i):
                print b[i].popleft(),
        
            if i>0:
                j=i-1
                while(j>-1):
                    print b[j].popleft(),
                    j-=1

        print '\r'