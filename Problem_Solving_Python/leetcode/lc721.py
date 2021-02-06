import unittest
from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        def add(name, email):
            if email not in parent:
                parent[email] = (name, email)

        def find(name, email):
            if email in parent:
                p = parent[email]
            else:
                p = (name, email)
            if (name, email)==p:
                return p

            par_name, par_email = parent[email]
            parent[email] = find(par_name, par_email)
            return parent[email]

        def union(name1, email1, name2, email2):
            add(name1, email1), add(name2, email2)
            p1, p2 = find(name1, email1), find(name2, email2)
            if p1!=p2:
                temp_email1, temp_email2 = p1[1], p2[1]
                parent[temp_email1] = parent[temp_email2]

        for account in accounts:
            name = account[0]
            emails = account[1:]
            for i,email in enumerate(emails):
                add(name, email)
                if i==0:
                    continue
                union(name, email, name, emails[i-1])


        # the dictionary looks like this : {('John', '1'): {'1', '2', '3'}, ('John', '101'): {'101'}, ('Mary', '999'): {'999'}})
        res = defaultdict(set)
        for account in accounts:
            emails = account[1:]
            for i, email in enumerate(emails):
                temp_par_name, temp_par_email = parent[email]
                true_par_name, true_par_email = find(temp_par_name, temp_par_email)
                res[(true_par_name,true_par_email)].add(email)



        res_list = [] # convert dictionary to list
        for name, email in res:
            temp = [name] + sorted(list(res[(name,email)]))
            res_list.append(temp)
        return res_list




class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = [["John",'1', '2', '3'],  ["John", "101"], ["Mary", "999"]]
        actual = sol.accountsMerge(accounts = [["John", "1", "2"], ["John", "101"], ["John", "1", "3"], ["Mary", "999"]])
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)