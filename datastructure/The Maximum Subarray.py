# -*- coding: utf-8 -*-
"""
Created on Mon May 30 14:55:27 2016

@author: kid

hackerrank Algorithms Dynamic Programming The Maximum Subarray
"""

def con_sub(a,s1,s2):
    if s1==s2:
        return [a[s1],s1,s1]
    else:
        a0,a1,a2=con_sub(a,s1,(s1+s2)/2)
        a00,a11,a22=con_sub(a,(s1+s2)/2+1,s2)
        
        if a0<=0 or a00<=0:
            if a0>a00:
                return [a0,a1,a2]
            else:
                return [a00,a11,a22]
                
        else:
            if a11==a2+1:
                return [a0+a00,a1,a22]
            else:
                tmp=0
                for i in range(a2+1,a11):
                    tmp+=a[i]
                
                if a0+a00+tmp>a0 and a0+a00+tmp>a00:
                    return [a0+a00+tmp,a1,a22]
                elif a0>a00:
                    return [a0,a1,a2]
                else:
                    return [a00,a11,a22]
                
a=input()
for _ in range(a):
    n=input()
    s=map(int,raw_input().strip().split())
    
    count=0
    Min=0
    key=False
    
    for i in range(len(s)):
        if s[i]>0:
            if not key:
                key=True
                count+=s[i]
            else:
                count+=s[i]
        else:
            if s[i]<Min:
                Min=s[i]
                
    s1,s2,s3=con_sub(s,0,len(s)-1)
    
    if key:
        print s1,count
    else:
        print Min,Min
