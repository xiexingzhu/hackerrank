# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 13:26:12 2016

@author: kid

hackerrank Algorithms Strings Common Child
"""

def commonchild(a,b):
    m=len(a)
    n=len(b)
    
    mat=[[0]*5001 for i in range(5001)]
    
    for i in range(m):
        for j in range(n):
            if a[i]==b[j]:
                mat[i+1][j+1]=mat[i][j]+1
            else:
                mat[i+1][j+1]=max(mat[i][j+1],mat[i+1][j])
                
    return mat[m][n] 
    
            
            
        

