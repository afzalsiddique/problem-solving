import unittest;


def get_sol(): return Solution()
class Solution:
    def parseBoolExpr(self, s: str) -> bool:
        def convert(c): # ['t'-> True, 'f'->False, True->True, False->False, '('->'(', '!'->'!']
            if c in [True,False]: return c
            if c=='t': return True
            if c=='f': return False
            return c
        def evaluate(li,op):
            if op=='|': return any(x==True for x in li)
            elif op=='&': return all(x==True for x in li)
            return not li[0]

        n=len(s)
        st = []
        i=0
        while i<n:
            while i<n and s[i]!=')': # add to stack until ')' is found
                if s[i]!=',': # ignore comma
                    st.append(convert(s[i]))
                i+=1
            if i<n and s[i]==')':
                li = []
                while st[-1]!='(':
                    li.append(st.pop())
                st.pop() # pop '('
                op=st.pop() # pop operator
                st.append(evaluate(li,op))
            i+=1
        return convert(st[0])
class Solution2:
    def parseBoolExpr(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c == ',': continue
            elif c == 't': stack.append(True)
            elif c == 'f': stack.append(False)
            elif c in ['&', '|', '!','(']: stack.append(c)
            elif c == ')':
                operands = set() # set will use less space
                while stack[-1] != '(':
                    operands.add(stack.pop())
                stack.pop() # pop out '('.
                operator = stack.pop()
                if operator == '&':
                    stack.append(all(operands))
                elif operator == '|':
                    stack.append(any(operands))
                elif operator == '!':
                    stack.append(not operands.pop())
        return stack.pop()
class Solution3:
    def parseBoolExpr(self, expression: str) -> bool:
        def doOps(li,sign):
            if sign=='!':
                return 't' if li[0]=='f' else 'f'
            res=False if sign=='|' else True
            for i in range(len(li)):
                x=True if li[i]=='t' else False
                if sign=='|':
                    res|=x
                else:
                    res&=x
            return 't' if res else 'f'
        st=[]
        for c in expression:
            if c in ',(': continue
            if c == ')':
                li=[]
                while st and st[-1] not in "!|&":
                    li.append(st.pop())
                sign=st.pop()
                tmp=doOps(li,sign)
                st.append(tmp)
            else:
                st.append(c)
        res=True if st[0]=='t' else False
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, get_sol().parseBoolExpr("!(f)"))
    def test2(self):
        self.assertEqual(True, get_sol().parseBoolExpr("|(f,t)"))
    def test3(self):
        self.assertEqual(False, get_sol().parseBoolExpr("&(t,f)"))
    def test4(self):
        self.assertEqual(False, get_sol().parseBoolExpr("&(t,f,t)"))
    def test5(self):
        self.assertEqual(False, get_sol().parseBoolExpr("!(t)"))
    def test6(self):
        self.assertEqual(False, get_sol().parseBoolExpr("|(&(t,f,t),!(t))"))
    def test7(self):
        self.assertEqual(False, get_sol().parseBoolExpr("&(|(f))"))
    def test8(self):
        self.assertEqual(True, get_sol().parseBoolExpr("|(f,f,f,t)"))
    def test9(self):
        self.assertEqual(True, get_sol().parseBoolExpr("!(&(f,t))"))
    def test10(self):
        self.assertEqual(True, get_sol().parseBoolExpr("&(t,t,t)"))
    def test11(self):
        self.assertEqual(True, get_sol().parseBoolExpr("|(f,&(t,t))"))
    def test12(self):
        self.assertEqual(False, get_sol().parseBoolExpr("!(&(!(&(f)),&(t),|(f,f,t)))"))
