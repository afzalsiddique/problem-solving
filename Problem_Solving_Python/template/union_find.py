# union find 1
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

# union find 2
root2 = {}
def find2(x):
    root2.setdefault(x, x)
    if x != root2[x]:
        root2[x] = find2(root2[x])
    return root2[x]
def union2(x, y):
    root2[find2(x)] = find2(y)