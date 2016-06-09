# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 14:50:17 2016

@author: kid

hackerrank Algorithms Strings Sherlock and Valid String
"""
from collections import Counter
<<<<<<< HEAD
def sherlock(a):
=======
def sherlock():
    a=raw_input()
>>>>>>> develop
    a=Counter(a)
    b=Counter(a.values()).most_common(1)[0][0]    
    
    count=0
    for i in a.values():
        if i==1 and b-i>1:
            count+=1
        elif i-b==1:
            count+=1
        else:
            count+=abs(i-b)
        

    
    print 'YES' if count<2 else 'NO'
    
    
