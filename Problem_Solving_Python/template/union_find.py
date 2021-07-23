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
    px,py = find(x), find(y)
    root[px]=root[py]
