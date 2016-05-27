# -*- coding: utf-8 -*-
"""
Created on Fri May 27 20:35:18 2016

@author: kid

hackerrank algotithm strings Bear and Steady Gene
"""
from collections import Counter

def smallest_substring(a):
    c=Counter(a)
    s1,s2,s3,s4=c['A'],c['C'],c['T'],c['G']
    
    n=len(a)/4
    tmp={}
    if s1>n:
        tmp['A']=s1-n
    if s2>n:
        tmp['C']=s2-n
    if s3>n:
        tmp['T']=s3-n
    if s4>n:
        tmp['G']=s4-n
        
    
    
    