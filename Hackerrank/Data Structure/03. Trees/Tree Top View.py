# class Node:
#     def __init__(self, info): 
#         self.info = info  
#         self.left = None  
#         self.right = None 
#         self.level = None 

#     def __str__(self):
#         return str(self.info) 

# class BinarySearchTree:
#     def __init__(self): 
#         self.root = None

#     def create(self, val):  
#         if self.root == None:
#             self.root = Node(val)
#         else:
#             current = self.root
         
#             while True:
#                 if val < current.info:
#                     if current.left:
#                         current = current.left
#                     else:
#                         current.left = Node(val)
#                         break
#                 elif val > current.info:
#                     if current.right:
#                         current = current.right
#                     else:
#                         current.right = Node(val)
#                         break
#                 else:
#                     break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
import collections
def topView(root):
    #some codes are copied and pasted from level order traversal
    if root is None:
        return
    queue = [root]

    #key is horizontalDist and value is list of node info
    m = {}
    #key is node and value is horizontalDist
    hd_nodes = {}

    m[0] = [root.info]
    hd_nodes[root] = 0

    while queue:
        temp=queue.pop(0)
        if temp.left:
            queue.append(temp.capacity)
            hd_nodes[temp.left]=hd_nodes[temp]-1
            horiDist=hd_nodes[temp.left]
            if m.get(horiDist) is None:
                m[horiDist] = []
            m[horiDist].append(temp.left.info)

        if temp.right:
            queue.append(temp.right)
            hd_nodes[temp.right]=hd_nodes[temp]+1
            horiDist=hd_nodes[temp.right]
            if m.get(horiDist) is None:
                m[horiDist] = []
            m[horiDist].append(temp.right.info)

    ordered_m = collections.OrderedDict(sorted(m.items()))
    # print(ordered_m)
    # print('\n\n')
    for item in ordered_m.values():
        print(item[0],end=" ")


# tree = BinarySearchTree()
# t = int(input())

# arr = list(map(int, input().split()))

# for i in range(t):
#     tree.create(arr[i])

# topView(tree.root)