import unittest;


def get_sol(): return Solution()
class Solution:
    def parseBoolExpr(self, s: str) -> bool:
        def performOperation(op,li):
            if op=='!': return not li[0]
            if op=='|': return any(x for x in li)
            return all(x for x in li)

        n=len(s)
        st = []
        OPS=['|','!','&']
        i=0
        while i<n:
            if s[i] in OPS:
                st.append(s[i])
            elif s[i]==')':
                li=[]
                while st[-1] not in OPS:
                    li.append(st.pop())
                op=st.pop()
                ans=performOperation(op,li)
                st.append(ans)
            elif s[i] in 'tf':
                st.append(True if s[i]=='t' else False)
            i+=1
        return st[-1]
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
