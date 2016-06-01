# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 15:28:50 2016

@author: kid

hackerrank Algorithms Dynamic Programming Candies
"""

s=input()
b=[1]*s
a=[]

for _ in range(s):
    a.append(input())
    
for i in range(0,len(a)-1):
    if a[i+1]>a[i]:
        b[i+1]=b[i]+1
      

for i in range(len(a)-1,0,-1):
    if a[i-1]>a[i] and b[i-1]<=b[i]:
        b[i-1]=b[i]+1

print sum(b)