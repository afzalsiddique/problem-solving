from collections import Counter
# union find class
class UnionFind: # if no of items at the time of instantiation, create a method add and use dict instead of array
    def __init__(self,n):
        self.n=n
        self.par=[i for i in range(n)]
        self.size=[1 for _ in range(n)]
    def __repr__(self): return str(self.par)
    def union(self,a,b):
        a=self.find(a)
        b=self.find(b)
        if a!=b:
            if self.size[a]<self.size[b]:
                a,b=b,a
            self.par[b]=a
            self.size[a]+=self.size[b]
    def find(self,a):
        if a!=self.par[a]:
            self.par[a]=self.find(self.par[a])
        return self.par[a]
    def size_of_groups(self):
        for a in range(self.n):
            self.find(a)
        count=Counter(self.par)
        return list(count.values())
class UnionFind2:
    def __init__(self):
        self.par={}
        self.size={}
    def __repr__(self): return str(self.par)
    def add(self,a):
        if a not in self.par:
            self.par[a]=a
            self.size[a]=1
    def union(self,a,b):
        self.add(a),self.add(b)
        a=self.find(a)
        b=self.find(b)
        if a!=b:
            if self.size[a]<self.size[b]:
                a,b=b,a
            self.par[b]=a
            self.size[a]+=self.size[b]
    def find(self,a):
        self.add(a)
        if a!=self.par[a]:
            self.par[a]=self.find(self.par[a])
        return self.par[a]
    def unionAll(self,li):
        if len(li)<1: return
        first=li[0]
        for second in li[1:]:
            self.union(first,second)
    def size_of_groups(self):
        for a in self.par:
            self.find(a)
        count=Counter(self.par.values())
        return list(count.values())
# union find 1
root = {}
def find(x):
    p=root.get(x,x)
    if p==x: return p
    root[x] = find(p)
    return root[x]
def union(x,y):
    root[find(x)]=find(y)

# union find 2
root = {}
def add(x):
    if x not in root:
        root[x] = x
def find(x):
    if x not in root:
        p = x
    else:
        p = root[x]
    if p==x:
        return p
    root[x] = find(root[x])
    return root[x]
def union(x,y):
    add(x),add(y)
    root[find(x)]=find(y)

# union find 3
root = {}
def find(x):
    root.setdefault(x, x)
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]
def union(x, y):
    root[find(x)] = find(y)