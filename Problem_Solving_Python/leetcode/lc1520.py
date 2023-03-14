import string;
from collections import defaultdict;
import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        def func(intervals:List[List[int]]): # maximum number of events can attend
            # print(intervals)
            ans=[]
            last=-1
            for start,end in intervals:
                if start>last:
                    ans.append([start,end])
                    last=end
            return ans

        n=len(s)
        left=defaultdict(lambda :n)
        right=defaultdict(lambda :-1)
        for i,c in enumerate(s):
            left[c]=min(left[c],i)
            right[c]=max(right[c],i)

        li=[]
        for c in string.ascii_lowercase:
            if c not in left: continue
            l=left[c]
            r=right[c]
            flag=True
            i=l
            while i<r+1:
                char=s[i]
                if left[char]<l:
                    flag=False
                    break
                r=max(r,right[char])
                i+=1
            if flag:
                li.append([l,r])
        li.sort(key=lambda x:(x[1],-x[0]))
        ans=func(li)
        res=[]
        for begin,end in ans:
            res.append(s[begin:end+1])
        return res

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(["e","f","ccc"], get_sol().maxNumOfSubstrings("adefaddaccc"))
    def test02(self):
        self.assertIn(get_sol().maxNumOfSubstrings("abbaccd"), [["d","bb","cc"],['bb', 'cc', 'd']])
    def test03(self):
        self.assertEqual(["abab"], get_sol().maxNumOfSubstrings("abab"))
    def test04(self):
        self.assertEqual(["cabcba"], get_sol().maxNumOfSubstrings("cabcba"))
    def test05(self):
        self.assertEqual(["bbcacbaba"], get_sol().maxNumOfSubstrings("bbcacbaba"))
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
