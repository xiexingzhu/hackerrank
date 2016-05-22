#binary search tree
#try using BST to do quick search

class Node:
    def __init__(self,value=None,left=None,right=None,parent=None):
        self.value=value
        self.left=left
        self.right=right
        self.parent=parent
    def insert(self,data):
        k=Node(data)
        tmp=self
        while tmp:
            Tmp=tmp
            if k.value<tmp.value:
                tmp=tmp.left
            else:
                tmp=tmp.right
        k.parent=Tmp
        if k.value<Tmp.value:
            Tmp.left=k
        else:
            Tmp.right=k
    def delete(self,z):
        if z.left==None:
            Transplant(z,z.right) 
        elif z.right==None:
            Transplant(z,z.left)
        else:
            y=Treeminimum(z.right)
            if not y.parent==z:
                Transplant(y,y.right)
                y.right=z.right
                y.right.parent=y
            Transplant(z,y)
            y.left=z.left
            y.left.parent=y
            
def Inordertreewalk(x):
    if not x==None:
        Inordertreewalk(x.left)
        print x.value
        Inordertreewalk(x.right)
def Treemaximum(x):
    while not x.right==None:
        x=x.right
    return x
def Treeminimum(x):
    while not x.left==None:
        x=x.left
    return x
def Transplant(u,v):
    if u==u.parent.left:
        u.parent.left=v
    else:
        u.parent.right=v
    if not v==None:
        v.parent=u.parent
        
        
def findroute(l,a,b,s):
    if b in l[a]:
        s.append(b)
        global tmp
        tmp=s
    else:
        for i in l[a]:
            if not i in s:
                ss=s[:]
                ss.append(i)
                findroute(l,str(i),b,ss)
                
            
