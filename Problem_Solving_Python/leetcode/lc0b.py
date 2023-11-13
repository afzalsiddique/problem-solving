from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
# from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
# from Problem_Solving_Python.template.binary_tree import deserialize,serialize
# def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y-20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x-dx, y-60, dx/2)
            jumpto(x, y-20)
            draw(node.right, x+dx, y-60, dx/2)
    import turtle
    t = turtle.Turtle()
    t.speed(0); turtle.delay(0)
    h = height(root)
    jumpto(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()

if __name__ == '__main__':
    drawtree(deserialize('[0,1,4,2,8,37,13,3,34,14,29,66,45,22,19,5,6,39,69,null,17,null,35,null,null,null,null,32,null,null,58,null,9,10,7,null,55,89,null,42,51,57,null,86,null,null,null,11,18,53,15,12,null,null,null,null,null,48,null,80,84,75,65,null,null,26,64,27,21,9]'))


# class Tester(unittest.TestCase):
#     def test1(self):
#         self.assertEqual([False,False,True],get_sol().areConnected(6, 2, [[1,4],[2,5],[3,6]]))
#     def test2(self):
#         self.assertEqual([True,True,True,True,True],get_sol().areConnected(6, 0,  [[4,5],[3,4],[3,2],[2,6],[1,3]]))
#     def test3(self):
#         self.assertEqual([False,False,False,False,False],get_sol().areConnected(5, 1, [[4,5],[4,5],[3,2],[2,3],[3,4]]))
#     def test4(self):
#         self.assertEqual([True,True,True,True,True,True],get_sol().areConnected(1000, 0, [[231,147],[877,685],[428,588],[654,7],[714,546],[693,965]]))
# def test5(self):
# def test6(self):
# def test7(self):
# def test8(self):
