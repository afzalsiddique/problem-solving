# https://leetcode.com/problems/accounts-merge/discuss/175269/My-Python-DFS-and-Union-Find-solutions-beats-98.7-and-100
import unittest
from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        # find root
        def findroot(i):
            while root[i] != i:
                root[i] = root[root[i]]  # path compression
                i = root[i]
            return i

        # union find
        d = {}  # key:val = email:index
        root = list(range(len(accounts)))
        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email in d:
                    r1, r2 = findroot(i), findroot(d[email])
                    root[r2] = r1
                else:
                    d[email] = i

        # merge accounts
        res0 = defaultdict(set)  # key:val = index: {set of emails}
        for i in range(len(accounts)):
            res0[findroot(i)] |= set(accounts[i][1:])

        # convert into required format
        res = []
        for k, v in res0.items():
            res.append([accounts[k][0]] + sorted(v))

        return res




class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = [["John",'1', '2', '3'],  ["John", "101"], ["Mary", "999"]]
        actual = sol.accountsMerge(accounts = [["John", "1", "2"], ["John", "101"], ["John", "1", "3"], ["Mary", "999"]])
        self.assertEqual(expected, actual)
