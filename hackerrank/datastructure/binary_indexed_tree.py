#here is a python code to implement 
#binary indexed tree
#which is very useful data structure
#in certain circumstances
#this has been commited to github
def get(BITree,i):
    s=0 #initialize result
    
    i=i+1#index in BITree is 1 more than the index in arr[]
    
    while i>0:
        s+= BITree[i]# add current element of BITree to sum
        i-=i & (-i)
    return s
    
#updated a node in BITree
def updatebit(BITree,n,i,v):
    
    i+=1
    
    while i <= n:
        BITree[i]+=v
        i+= i & (-i)
        
def construct(arr,n):
    BITree=[0]*(n+1) # Create and initialize BITree as 0
    
    for i in range(n):
        updatebit(BITree,n,i,arr[i])
        
    return BITree