# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 21:05:57 2016

@author: kid

hackerrank Algorithms Sorting Bigger is Greater
"""
def next_permutation(arr):
    
    arr=list(arr)
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return 'no answer'
    
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return ''.join(arr)

for _ in range(input()):
    print next_permutation(raw_input())
    

