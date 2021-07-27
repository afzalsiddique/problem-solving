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