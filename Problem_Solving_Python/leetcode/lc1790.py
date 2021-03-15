import unittest
from typing import List
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:return True

        l1,l2=list(s1),list(s2)
        for i in range(len(s1)):
            for j in range(len(s2)):
                l1[i],l1[j]=l1[j],l1[i]
                if l1==l2:return True
                l1[i],l1[j]=l1[j],l1[i]
        return False

class MyTestCase(unittest.TestCase):

    def test_1(self):
        actual =Solution().areAlmostEqual(s1 = "bank", s2 = "kanb")
        expected = True
        self.assertEqual(expected, actual)
