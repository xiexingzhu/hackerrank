# -*- coding: utf-8 -*-
def sumlen(a):
    tmp=[[a[0],1]]
    count=1
    
    for i in range(1,len(a)):
        Count=0
        while(len(tmp)>0 and a[i]>tmp[-1][0]):
            Count+=tmp[-1][1]
            tmp.pop()
        Count+=1
        tmp.append([a[i],Count])
        count+=Count
        
    return count
    
def sumper(a):
    a=list(permutations(a))
    count=0
    for i in range(len(a)):
        count+=sumlen(a[i])
        
    return '%.2f'%(float(count)/len(a))
