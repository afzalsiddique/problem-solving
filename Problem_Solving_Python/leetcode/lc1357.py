import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(n,d,p,c): return Cashier(n,d,p,c)
class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.cost={}
        self.order_no=0
        self.discount=discount
        self.n=n
        for i in range(len(products)):
            p_id,price=products[i],prices[i]
            self.cost[p_id]=price
    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.order_no=(self.order_no+1)%self.n
        total=0.0
        for i in range(len(product)):
            p_id,am=product[i],amount[i]
            total+=self.cost[p_id]*am
        if self.order_no==0:
            return total*(100-self.discount)/100
        return total


class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='Cashier':
                obj = get_sol(input[0],input[1],input[2],input[3])
                outputs.append(None)
            elif cmd=='getBill':
                outputs.append(obj.getBill(input[0],input[1]))
        return outputs
    def test_01(self):
        commands = ["Cashier","getBill","getBill","getBill","getBill","getBill","getBill","getBill"]
        inputs=[[3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]],[[1,2],[1,2]],[[3,7],[10,10]],[[1,2,3,4,5,6,7],[1,1,1,1,1,1,1]],[[4],[10]],[[7,3],[10,10]],[[7,5,3,1,6,4,2],[10,10,10,9,9,9,7]],[[2,3,5],[5,3,2]]]
        expected = [None,500.0,4000.0,800.0,4000.0,4000.0,7350.0,2500.0]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
