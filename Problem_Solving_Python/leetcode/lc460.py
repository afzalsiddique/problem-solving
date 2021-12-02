import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(x): return LFUCache(x)
# https://leetcode.com/problems/lfu-cache/discuss/800188/Python-O(1)-using-DLL-and-Dictionary
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None
    def __repr__(self): return str(self.val) + "->" + str(self.next)
class DLL:
    def __init__(self):
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def __repr__(self): return str(self.head.val) + "->" + str(self.head.next)
    def insertHead(self, node):
        headNext = self.head.next
        headNext.prev = node
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        self.size += 1

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1

    def removeTail(self):
        tail = self.tail.prev
        self.removeNode(tail)
        return tail


class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.freqTable = defaultdict(DLL)
        self.capacity = capacity
        self.minFreq = 0


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        return self.updateCache(key, self.cache[key].val)


    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return
        if key in self.cache:
            self.updateCache(key, value)
        else:
            if len(self.cache) == self.capacity:
                prevTail = self.freqTable[self.minFreq].removeTail()
                del self.cache[prevTail.key]
            node = ListNode(key, value)
            self.freqTable[1].insertHead(node)
            self.cache[key] = node
            self.minFreq = 1


    def updateCache(self, key, value):
        node = self.cache[key]
        node.val = value
        prevFreq = node.freq_count
        self.freqTable[node.freq_count].removeNode(node)
        node.freq_count += 1
        self.freqTable[node.freq_count].insertHead(node)
        if prevFreq == self.minFreq and self.freqTable[prevFreq].size == 0:
            self.minFreq += 1
        return node.val



class tester(unittest.TestCase):
    def test1(self):
        commands = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
        inputs = [[2],        [1, 1], [2, 2], [1],   [3, 3], [2],   [3],  [4, 4], [1],  [3],   [4]]
        exptected = [None, None, None, 1, None, -1, 3, None, -1, 3, 4]
        outputs = []
        for c,i in zip(commands, inputs):
            if c == 'LFUCache':
                obj = get_sol(i[0])
                outputs.append(None)
            elif c =='put': outputs.append(obj.put(i[0],i[1]))
            else: outputs.append(obj.get(i[0]))
        self.assertEqual(exptected,outputs)
