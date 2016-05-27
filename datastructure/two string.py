# -*- coding: utf-8 -*-
"""
Created on Fri May 27 20:13:04 2016

@author: kid

hackerrank algorithm strings two string 
"""

def twostring(a,b):
    a=set(a)
    b=set(b)
    
    print 'YES' if a&b else 'NO'
    

