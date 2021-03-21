from typing import List


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
# def checkOnesSegment(s: str) -> bool:
        started = False
        second = False
        for c in s:
            if second==True and c=='1':
                return False
            if started==True and c=='0':
                second = True
            if started==False and c=='1':
                started=True
        return True

# print(checkOnesSegment('1001'),False)
# print(checkOnesSegment('0011'),True)
# print(checkOnesSegment('1111'), True)
# print(checkOnesSegment('1110'), True)
# print(checkOnesSegment('101001'), False)
# print(checkOnesSegment('010101'), False)
# print(checkOnesSegment('111111'), True)
# print(checkOnesSegment('000000'), True)
# print(checkOnesSegment('1'), True)
# print(checkOnesSegment('0'), True)
# print(checkOnesSegment('00'), True)
# print(checkOnesSegment('11'), True)
#
