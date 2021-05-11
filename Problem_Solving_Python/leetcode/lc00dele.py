import itertools
import math
import operator
import random
from bisect import *
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()

class Solution:
    def isValidSerialization(self, preorder)-> bool:
        # remember how many empty slots we have
        # non-null nodes occupy one slot but create two new slots
        # null nodes occupy one slot

        p = preorder.split(',')

        #initially we have one empty slot to put the root in it
        slot = 1
        for node in p:
            # no empty slot to put the current node
            if slot == 0:
                return False
            # occupy slot (null nodes and non-null nodes occupy slots)
            slot-=1

            # only non-null nodes create slots
            if node!='#':
                slot += 2

        #we don't allow empty slots at the end
        return slot==0

class mytestcase(unittest.TestCase):
    def test1_1(self):
        preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
        Output= True
        self.assertEqual(Output,get_sol().isValidSerialization(preorder))
    def test1_2(self):
        preorder = "1,#"
        Output= False
        self.assertEqual(Output,get_sol().isValidSerialization(preorder))
    def test1_3(self):
        preorder = "9,#,#,1"
        Output= False
        self.assertEqual(Output,get_sol().isValidSerialization(preorder))
