# s = "[({{[])})]"
# s = '[(([]})})]'
# s = '[({({[]})]'
# s = '[(]{({})]'
s = '[]'
def func(s):
    while(s):
        sOld = s
        s = s.replace('[]','')
        s = s.replace('{}','')
        s = s.replace('()','')
        print(s)
        if sOld == s:
            return False
    return True
func(s)