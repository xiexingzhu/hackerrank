# -*- coding: utf-8 -*-
"""
Created on Fri May 27 20:35:18 2016

@author: kid

hackerrank algotithm strings Bear and Steady Gene
"""
from collections import Counter

def smallest_substring(a):
    c=Counter(a)
    if 'A' in c:
        s1=c['A']
    else:
        s1=0
    if 'C' in c:
        s2=c['C']
    else:
        s2=0
    if 'T' in c:
        s3=c['T']
    else:
        s3=0
    if 'G' in c:
        s4=c['G']
    else:
        s4=0
   
    Min=-1
    Max=-1
    count=0
    
    n=len(a)/4
    
    if s1==n and s2==n and s3==n and s4==n:
        return 0
    
    tmp={}
    key=False
    if s1>n:
        tmp['A']=[-1]*(s1-n)
    if s2>n:
        tmp['C']=[-1]*(s2-n)
    if s3>n:
        tmp['T']=[-1]*(s3-n)
    if s4>n:
        tmp['G']=[-1]*(s4-n)
        
    for i in range(len(a)):
        if a[i] in tmp:
            if key:
                Max=i
                tmp[a[i]].append(i)
                if tmp[a[i]][0]==Min:
                    del tmp[a[i]][0]
                
                    Min=min([Tmp[0] for Tmp in tmp.values()])
                    if Max-Min<count:
                        count=Max-Min
                else:
                    del tmp[a[i]][0] 
                    if Max-Min<count:
                        count=Max-Min
            else:
                Max=i
                tmp[a[i]].append(i)
                del tmp[a[i]][0]

                
                Min=min([Tmp[0] for Tmp in tmp.values()])
                if Min>=0:
                    count=Max-Min
                    key=True
                    
    return count+1
        
    
    
        
    
    
    