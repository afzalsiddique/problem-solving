""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
minn, maxx = -999999, 999999
def check_binary_search_tree_(root):   
    return isBSTUtil(root, minn, maxx)
def isBSTUtil(root, minn, maxx):
    if root is None:
        return True
    if root.data<minn or root.data>maxx:
        return False
    return isBSTUtil(root.left, minn, root.data-1) and isBSTUtil(root.right, root.data+1, maxx)
