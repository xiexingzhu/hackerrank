# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 19:00:26 2016

@author: kid

hackerrank Algorithms Sorting Counting Sort
"""
def countingsort(arr):
    count=[0]*100
    for i in range(len(arr)):
        count[arr[i]]+=1
        
    for i in range(len(count)):
        if not count[i]==0:
            j=count[i]
            while(j>0):
                print i,
                j-=1
                
    return ''
