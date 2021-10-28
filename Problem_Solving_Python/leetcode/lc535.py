import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Codec()
class Codec:
    def __init__(self):
        self.website = 'www.tinyurl.com/'
        self.chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        self.short_to_long ={}
        self.long_to_short = {}
        self.LENGTH=6
    def get_code(self):
        code = [random.choice(self.chars) for _ in range(self.LENGTH)]
        return ''.join(code)
    def encode(self, longUrl: str) -> str:
        if longUrl in self.long_to_short:
            return self.long_to_short[longUrl]
        shortUrl = self.get_code()
        while shortUrl in self.short_to_long:
            shortUrl = self.get_code()
        self.long_to_short[longUrl] = shortUrl
        self.short_to_long[shortUrl]=longUrl
        return self.website+shortUrl
    def decode(self, shortUrl: str) -> str:
        shortUrl = shortUrl[-6:]
        return self.short_to_long[shortUrl]
class Codec2:
    # problem: If I'm asked to encode the same long URL several times, it will get several entries. That wastes codes and memory.
    def __init__(self):
        self.chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        self.short_to_long ={}
        self.LENGTH = 6
    def get_code(self):
        code = [random.choice(self.chars) for _ in range(self.LENGTH)]
        return ''.join(code)
    def encode(self, longUrl: str) -> str:
        shortUrl = self.get_code()
        while shortUrl in self.short_to_long:
            shortUrl = self.get_code()
        self.short_to_long[shortUrl]=longUrl
        return shortUrl
    def decode(self, shortUrl: str) -> str:
        return self.short_to_long[shortUrl]

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='Codec':
                obj = get_sol()
                outputs.append(None)
            elif cmd=='do':
                shortUrl = obj.encode(input[0])
                longUrl = obj.decode(shortUrl)
                outputs.append(longUrl)
        return outputs
    def test_01(self):
        commands = ["Codec","do"]
        x = 'www.leetcode.com'
        inputs=[      [],  [x]]
        expected = [None, x]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_02(self):
        commands = ["Codec","do","do"]
        x = 'www.leetcode.com'
        inputs=[      [],  [x],[x]]
        expected = [None,   x,  x]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
