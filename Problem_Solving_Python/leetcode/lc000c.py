import string;
from collections import Counter;
import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def makeKey(count:Counter):
            li=[]
            for c in sorted(count.keys()):
                if count[c]==0: continue
                li.append(c+':'+str(count[c]))
            return ' '.join(li)
        def makeKeyOneLess(count:Counter, c:str):
            count[c]-=1
            res=makeKey(count)
            count[c]+=1
            return res
        def valid(count:Counter):
            for c in string.ascii_lowercase:
                if makeKeyOneLess(count,c) in sett:
                    return True
            return False

        sett=set()
        for start in startWords:
            sett.add(makeKey(Counter(start)))

        res=0
        for tar in targetWords:
            if valid(Counter(tar)):
                res+=1
        return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().wordCount(["ant","act","tack"], ["tack","act","acti"]))
    def test2(self):
        self.assertEqual(1, get_sol().wordCount(startWords = ["ab","a"], targetWords = ["abc","abcd"]))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
