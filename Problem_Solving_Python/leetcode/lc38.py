import unittest
class Solution:
    def countAndSay(self, n: int) -> str:
        def helper(s:str):
            result = []
            j=0
            i=0
            while i<len(s):
                if i>0 and s[i]!=s[i-1]:
                    result.append(str(i-j) + s[j])
                    j=i
                i+=1
            result.append(str(i-j)+s[j])
            return "".join(result)


        if n==1:return "1"
        temp = '1'
        for i in range(n-1):
            temp = helper(temp)
        return temp


    def countAndSay__(self, n: int) -> str:
        result = '1'
        for _ in range(1,n):
            result = self.string_build(result)
        return result
    def string_build(self, s):
        ptr = 0
        res = []
        n = len(s)
        while ptr<n:
            ch = s[ptr]
            cnt = 0
            while ptr<n and ch==s[ptr]:
                cnt += 1
                ptr +=1
            res.append(str(cnt))
            res.append(ch)
        return "".join(res)


    # less readable
    def countAndSay_(self, n: int) -> str:
        s = "1 "
        result = []
        for _ in range(n-1):
            l,r=0,0
            while s[r]!=' ':
                while s[l]==s[r]:
                    r+=1
                result.append(str(r-l))
                result.append(s[l])
                l=r
            result.append(" ")
            s = "".join(str(x) for x in result)
            result = []
            # print(s)
        return s[:-1]





class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual('1',Solution().countAndSay(1))
    def test_2(self):
        self.assertEqual('11',Solution().countAndSay(2))
    def test_3(self):
        self.assertEqual('21',Solution().countAndSay(3))
    def test_4(self):
        self.assertEqual('1211',Solution().countAndSay(4))
    def test_5(self):
        self.assertEqual('111221',Solution().countAndSay(5))
    def test_6(self):
        self.assertEqual('312211',Solution().countAndSay(6))
