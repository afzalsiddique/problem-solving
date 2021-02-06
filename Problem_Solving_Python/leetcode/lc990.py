import unittest
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
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
            if px!=py:
                root[px]=root[py]

        equal_sign = [(s[0],s[3]) for s in equations if s[1]=='=']
        not_equal_sign = [(s[0],s[3]) for s in equations if s[1]=='!']

        # if x==y then x and y will belong to the same component
        for x,y in equal_sign:
            union(x,y)

        # if x!=y then x and y will belong the different components
        for x,y in not_equal_sign:
            root_a, root_b = find(x), find(y)
            if root_a==root_b:
                return False
        return True



class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = False
        actual = sol.equationsPossible(["a==b","b!=a"])
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = True
        actual = sol.equationsPossible(["b==a","a==b"])
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = True
        actual = sol.equationsPossible(["a==b","b==c","a==c"])
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = False
        actual = sol.equationsPossible(["a==b","b!=c","c==a"])
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = True
        actual = sol.equationsPossible(["c==c","b==d","x!=z"])
        self.assertEqual(expected, actual)

