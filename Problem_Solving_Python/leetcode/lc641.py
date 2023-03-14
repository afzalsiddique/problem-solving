import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(k): return MyCircularDeque(k)
class MyCircularDeque:
    def __init__(self, k: int):
        self.k=k
        self.left=k
        self.li = [0]*k
        self.beginAndEnd=[0,-1]
    def helper(self, dir, value=None):
        isInsertOperation=value!=None
        if isInsertOperation:
            if self.isFull(): return False
        else:
            if self.isEmpty(): return False

        if isInsertOperation:
            idx=0 if dir==-1 else 1 # begin pointer should
        else:
            idx=1 if dir==-1 else 0

        self.beginAndEnd[idx]=(self.beginAndEnd[idx]+dir)%self.k

        if isInsertOperation:
            self.li[self.beginAndEnd[idx]]=value
            self.left-=1
        else:
            self.left+=1
        return True
    def insertFront(self, value: int) -> bool:
        return self.helper(-1, value)
    def insertLast(self, value: int) -> bool:
        return self.helper(1, value)
    def deleteFront(self) -> bool:
        return self.helper(1)
    def deleteLast(self) -> bool:
        return self.helper(-1)
    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.li[self.beginAndEnd[0]]
    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.li[self.beginAndEnd[1]]
    def isEmpty(self) -> bool:
        return self.left==self.k
    def isFull(self) -> bool:
        return self.left==0
class MyCircularDeque2:
    def __init__(self, k: int):
        self.k=k
        self.begin=0
        self.end=-1
        self.li=[-1]*k
        self.left=k
    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        self.left-=1
        self.begin=(self.begin-1)%self.k
        self.li[self.begin]=value
        return True
    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        self.left-=1
        self.end=(self.end+1)%self.k
        self.li[self.end]=value
        return True
    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.left+=1
        self.begin=(self.begin+1)%self.k
        return True
    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.left+=1
        self.end=(self.end-1)%self.k
        return True
    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.li[self.begin]
    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.li[self.end]
    def isEmpty(self) -> bool:
        return self.left == self.k
    def isFull(self) -> bool:
        return self.left == 0


class MyCircularDeque2:
    def __init__(self, k: int):
        self.capacity = k
        self.left=k

        self.start=1
        self.end=0
        # also works
        self.start=0
        self.end=-1

        self.q=[-1]*k
    def insertFront(self, value: int) -> bool:
        q=self.q
        if self.isFull(): return False
        self.start-=1
        self.start%=self.capacity
        q[self.start]=value
        self.left-=1
        return True
    def insertLast(self, value: int) -> bool:
        q=self.q
        if self.isFull():
            return False
        self.end+=1
        self.end%=self.capacity
        q[self.end]=value
        self.left-=1
        return True
    def deleteFront(self) -> bool:
        q=self.q
        if self.isEmpty():
            return False
        q[self.start]=-1
        self.start+=1
        self.start%=self.capacity
        self.left+=1
        return True
    def deleteLast(self) -> bool:
        q=self.q
        if self.isEmpty():
            return False
        q[self.end]=-1
        self.end-=1
        self.end%=self.capacity
        self.left+=1
        return True
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.start]
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.end]
    def isEmpty(self) -> bool:
        if self.left==self.capacity: return True
        return False
    def isFull(self) -> bool:
        if self.left: return False
        return True
class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='MyCircularDeque':
                obj = get_sol(input[0])
                outputs.append(None)
            elif cmd=='insertFront':
                outputs.append(obj.insertFront(input[0]))
            elif cmd=='insertLast':
                outputs.append(obj.insertLast(input[0]))
            elif cmd=='getFront':
                outputs.append(obj.getFront())
            elif cmd=='getRear':
                outputs.append(obj.getRear())
            elif cmd=='deleteFront':
                outputs.append(obj.deleteFront())
            elif cmd=='deleteLast':
                outputs.append(obj.deleteLast())
            elif cmd=='isFull':
                outputs.append(obj.isFull())
            elif cmd=='isEmpty':
                outputs.append(obj.isEmpty())
        return outputs
    def test01(self):
        commands = ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
        inputs=[[3], [1], [2], [3], [4], [], [], [], [4], []]
        exptected = [None, True, True, True, False, 2, True, True, True, 4]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(exptected,outputs)
    def test02(self):
        commands = ["MyCircularDeque","insertFront","insertLast","getFront","insertLast","getFront","insertFront","getRear","getFront","getFront","deleteLast","getRear"]
        inputs=[       [5],              [7],          [0],         [],        [3],        [],          [9],         [],       [],         [],        [],        []]
        exptected = [None,              True,          True,        7,        True,        7,          True,           3,      9,          9,         True,      0]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(exptected,outputs)
    def test03(self):
        commands = ["MyCircularDeque","insertFront","insertLast","insertLast","getFront","deleteLast","getRear","insertFront","deleteFront","getRear","insertLast","isFull"]
        inputs=[[3],[8],[8],[2],[],[],[],[9],[],[],[2],[]]
        exptected = [None,True,True,True,8,True,8,True,True,8,True,True]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(exptected,outputs)
    def test04(self):
        commands = ["MyCircularDeque","insertFront","insertFront","insertLast","deleteLast","insertLast","getRear","insertLast","getFront","deleteFront","insertLast","insertLast"]
        inputs=[[5],[5],[0],[5],[],[7],[],[7],[],[],[6],[1]]
        exptected = [None,True,True,True,True,True,7,True,0,True,True,True]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(exptected,outputs)
    def test05(self):
        commands = ["MyCircularDeque","insertFront","insertFront","isEmpty","insertLast","insertLast","getRear","insertFront","insertFront","getRear","insertFront","insertFront","insertLast","getRear","insertLast","insertFront","getRear","getRear","getFront","getFront","insertFront","deleteLast","insertFront","getRear","deleteLast","getFront","insertLast","getFront","getFront","insertFront","insertFront","deleteLast","deleteFront","getRear","insertFront","getFront","getFront","insertFront","getRear","getRear","isFull","getFront","getFront","insertLast","insertLast","isFull","getRear","getFront","getFront","isFull","getFront","deleteLast","deleteFront","isFull","insertFront","deleteFront","deleteFront","insertFront","isEmpty","getRear","insertFront","getFront","insertFront","deleteLast","getRear","getFront","getFront","isEmpty","isEmpty","deleteFront","insertLast","deleteFront","getFront","getRear","isFull","insertLast","getRear","insertFront","getFront","insertFront","getFront","getFront","getRear","getFront","insertFront","deleteLast","insertLast","insertLast","deleteFront","getRear","getRear","getRear","insertFront","isFull","getRear","isFull","insertFront","insertLast","getRear","deleteFront","deleteFront","getRear","getFront","insertLast","getRear","getFront","getFront","getFront","insertLast","insertLast","isEmpty","insertLast","insertFront","isFull","deleteFront","isFull","getFront","insertLast","deleteFront","getFront","insertFront","deleteFront","getRear","deleteFront","getRear","insertLast","getRear","getFront","getRear","getFront","insertFront","getFront","deleteLast","insertFront","isEmpty","getRear","getRear","getFront","isFull","insertFront","insertLast","deleteFront","isEmpty","insertFront","getFront","getRear","getFront","insertLast","insertFront","insertFront","deleteLast","getRear","getRear","getRear","insertLast","getRear","getRear","getFront","getFront","insertFront","deleteLast","getFront","getRear","getRear","deleteLast","deleteLast","deleteFront","deleteFront","getRear","getRear","deleteFront","getRear","getFront","insertLast","getFront","getRear","getRear","insertFront","isFull","insertLast","getFront","isFull","insertFront","getRear","insertLast","getFront","insertFront","insertFront","getRear","deleteLast","getFront","getFront","getFront","insertFront","isEmpty","insertFront","deleteLast","getRear","insertFront","insertFront","insertLast","insertLast","getFront","insertFront","insertFront","insertLast","getRear","getFront","insertLast","isEmpty","isFull","insertFront","getFront","getFront","deleteFront","insertFront","getRear","getRear","isEmpty","getFront","isEmpty","insertLast","getFront","isEmpty","insertLast","getFront","deleteLast","getRear","getFront","insertLast","getFront","insertFront","getFront","getFront","getRear","getRear","getFront","getRear","getFront","insertLast","insertFront","isFull","deleteFront","getRear","insertFront","insertLast","getFront","isFull","deleteLast","insertFront","insertLast","insertLast","insertFront","getFront","deleteFront","insertLast","getFront","isFull","getFront","insertLast","insertLast","getFront","getFront","getRear","insertFront","deleteFront","getFront","deleteFront","getFront","insertLast","getRear","getRear","insertLast","insertFront","insertFront","insertLast","getFront","insertLast","getRear","getRear","getFront","insertLast","insertFront","insertLast","insertFront","insertFront","getFront","deleteFront","deleteLast","insertLast","deleteLast","insertLast","insertLast","insertLast","insertFront","deleteLast","insertLast","isFull","getFront","insertFront","deleteLast","getFront","getFront","insertFront","insertFront","insertLast","getFront","getFront","getRear","getFront","insertFront","getRear","getFront","insertFront","getFront","getRear","getFront","insertLast","deleteLast","insertFront","getFront","getFront","insertLast","getRear","insertFront","getFront","deleteFront","getFront","deleteFront","insertLast","getRear","insertLast","isFull","getRear","getFront","deleteFront","getRear","getRear","insertLast","isEmpty","insertLast","insertFront","getRear","insertLast","getFront","getFront","getFront","insertFront","getRear","deleteFront","isEmpty","isEmpty","insertFront","insertLast","insertLast","isFull","insertLast","getRear","deleteFront","deleteFront","getRear","isFull","insertFront","getFront","isFull","getFront","getRear","insertFront","getFront","getRear","getRear","getRear","deleteLast","insertFront","insertFront","insertFront","insertLast","insertLast","deleteFront","getFront","insertFront","insertFront","insertLast","getFront","insertFront","deleteFront","getFront","insertFront","insertLast","deleteLast","getFront","getRear","getRear","getFront","getFront","getFront","getFront","insertLast","getRear","deleteLast","getRear","getFront","getFront","insertLast","getFront","deleteFront","deleteLast","getFront","isEmpty","getFront","insertFront","insertFront","insertLast","getRear","deleteFront","isFull","getFront","getFront","getRear","insertFront","deleteFront","insertLast","getFront","deleteLast","getRear","deleteLast","insertLast","insertFront","getRear","insertFront","getRear","getFront","insertLast","getFront","insertLast","insertLast","isEmpty","getRear","deleteFront","getRear","deleteLast","insertFront","getRear","insertFront","insertLast","insertLast","insertLast","insertFront","getRear","insertLast","isEmpty","getRear","insertFront","insertLast","deleteFront","insertFront","insertFront","getRear","insertFront","deleteFront","getFront","isEmpty","insertLast","deleteFront","deleteFront","getFront","deleteFront","insertLast","getFront","insertLast","isFull","insertLast","insertFront","getFront","getFront","getRear","insertLast","deleteLast","getFront","getRear","deleteFront","insertLast","insertLast","insertLast","getFront","deleteFront","isFull","insertFront","getRear","insertLast","getRear","getFront","getRear","getRear","getFront","getFront","insertLast","isFull","getRear","isEmpty","getRear","isEmpty","insertFront","insertFront","getRear","insertLast","getRear","insertLast","isFull","getFront","getFront","getFront","insertLast","getRear","getFront","deleteLast","insertFront","getFront","getFront","getRear","getFront","insertFront","getFront","getRear","getFront","deleteFront","insertLast","deleteLast","insertLast","insertLast","getRear","insertLast","getRear","getRear","getRear","getRear","insertFront","getRear","insertFront","getFront","getFront","insertFront","insertFront","deleteFront","getFront","insertFront","getRear","deleteFront","getRear","isFull","insertFront","getRear","isFull","getFront","getRear","insertFront","getFront","insertFront","getRear","getFront","deleteFront","getFront","insertFront","deleteLast","insertFront","getFront","getFront","insertFront","insertLast","getFront","isFull","getRear","insertLast","getRear","isEmpty","insertLast","insertFront","isEmpty","getFront","getRear","insertFront","insertFront","getRear","insertFront","deleteLast","isEmpty","getFront","getRear","insertFront","getFront","insertFront","getRear","insertFront","getFront","insertLast","getFront","getFront","getFront","deleteFront","insertLast","getFront","getFront","deleteFront","getRear","getRear","getFront","deleteLast","insertFront","getRear","getFront","insertLast","insertLast","getFront","insertLast","getFront","isFull","getRear","getFront","insertFront","insertLast","getFront","deleteFront","insertFront","insertLast","insertLast","getRear","getFront","getRear","insertFront","insertLast","getRear","insertFront","insertLast","deleteFront","getFront","getRear","insertFront","insertFront","deleteFront","insertFront","getRear","getFront","getFront","getRear","insertLast","insertFront","insertFront","deleteLast","insertLast","isFull","getRear","getFront","insertFront","insertLast","deleteFront","getRear","getRear","getFront","getRear","getRear","insertLast","isFull","isEmpty","insertLast","deleteFront","deleteFront","insertLast","insertLast","insertLast","insertFront","insertFront","insertFront","getFront","getFront","deleteFront","getFront","isFull","deleteFront","insertFront","getFront","deleteLast","deleteLast","getFront","getFront","insertFront","insertLast","insertFront","insertFront","insertLast","deleteFront","insertFront","getRear","deleteLast","insertFront","insertLast","insertLast","insertFront","getRear","getRear","deleteLast","insertLast","isFull","insertFront","getFront","getRear","getRear","insertLast","getRear","insertLast","deleteLast","deleteLast","isEmpty","insertFront","getFront","deleteLast","getRear","isEmpty","insertLast","getRear","getRear","deleteLast","isEmpty","getFront","getRear","insertFront","getFront","deleteFront","getRear","insertLast","getFront","getFront","insertFront","insertLast","getRear","getRear","getRear","insertLast","deleteLast","insertLast","isEmpty","insertLast","deleteLast","getFront","getRear","insertLast","insertFront","insertLast","getRear","insertFront","getFront","deleteFront","deleteLast","insertFront","insertFront","deleteLast","getRear","deleteLast","getFront","insertLast","getRear","isEmpty","deleteLast","deleteFront","insertFront","insertLast","isEmpty","getFront","insertLast","getRear","getFront","isFull","getFront","getFront","getRear","isFull","getFront","getRear","getFront","isEmpty","getFront","insertLast","isFull","insertFront","insertLast","getFront","getRear","insertFront","getFront","insertFront","getFront","getRear","isFull","insertFront","insertLast","getRear","insertLast","getFront","getFront","getFront","insertLast","insertFront","insertLast","getRear","getRear","getRear","getFront","getFront","insertFront","insertLast","insertLast","getRear","getFront","getFront","insertLast","getFront","getRear","insertFront","insertLast","getFront","getRear","getRear","insertFront","insertLast","insertLast","insertFront","getRear","isEmpty","getFront","isFull","insertFront","deleteLast","insertFront","insertLast","getRear","insertLast","getRear","getFront","insertFront","deleteLast","getRear","insertFront","deleteLast","insertFront","insertLast","deleteLast","insertLast","insertFront","insertLast","deleteFront","insertFront","deleteLast","insertLast","getFront","insertLast","deleteFront","deleteFront","getFront","insertLast","insertLast","getFront","insertLast","insertFront","isEmpty","getRear","getFront","insertFront","getFront","isFull","insertLast","getFront","isEmpty","isEmpty","deleteFront","insertLast","insertFront","getFront","insertFront","getRear","insertFront","isFull","insertFront","insertLast","getFront","insertFront","insertFront","insertLast","isFull","getRear","insertLast","getFront","getRear","getRear","insertFront","getRear","getRear","deleteLast","getFront","insertFront","insertFront","isFull","getFront","isEmpty","getRear","deleteFront","getFront","getFront","getFront","isEmpty","getRear","insertFront","getRear","getFront","insertFront","insertFront","insertFront","insertLast","insertLast","getRear","getFront","insertLast","insertLast","insertLast","insertLast","insertFront","getFront","getRear","getRear","insertLast","insertLast","insertFront","insertFront","deleteFront","insertFront","insertFront","isFull","getRear","insertFront","deleteFront","deleteFront","deleteFront","getFront","getFront","insertFront","getFront","getFront","isFull","isEmpty","getRear","insertLast","isEmpty","getFront","insertFront","insertFront","getFront","getFront","getFront","insertLast","deleteFront","isEmpty","getRear","insertFront","insertLast","insertLast","insertLast","getRear","insertLast","getRear","getRear","getFront","insertLast","getRear","getRear","getFront","insertLast","getFront","insertFront","isFull","getRear","insertLast","isFull","getRear","getRear","insertLast","insertFront","getFront","isEmpty","insertLast","insertFront","getRear","insertLast","insertLast","insertLast","getRear","deleteLast","getFront","getFront","deleteFront","insertFront","isFull","isFull","insertFront","deleteLast"]
        inputs=[[461],[848],[637],[],[573],[28],[],[413],[674],[],[320],[443],[703],[],[678],[34],[],[],[],[],[430],[],[935],[],[],[],[581],[],[],[693],[46],[],[],[],[105],[],[],[65],[],[],[],[],[],[421],[420],[],[],[],[],[],[],[],[],[],[257],[],[],[686],[],[],[813],[],[835],[],[],[],[],[],[],[],[860],[],[],[],[],[991],[],[79],[],[930],[],[],[],[],[221],[],[794],[759],[],[],[],[],[249],[],[],[],[366],[746],[],[],[],[],[],[951],[],[],[],[],[355],[301],[],[391],[659],[],[],[],[],[772],[],[],[2],[],[],[],[],[315],[],[],[],[],[908],[],[],[271],[],[],[],[],[],[605],[806],[],[],[593],[],[],[],[460],[438],[501],[],[],[],[],[411],[],[],[],[],[64],[],[],[],[],[],[],[],[],[],[],[],[],[],[171],[],[],[],[315],[],[742],[],[],[227],[],[845],[],[886],[668],[],[],[],[],[],[50],[],[24],[],[],[486],[293],[495],[497],[],[624],[220],[65],[],[],[781],[],[],[643],[],[],[],[909],[],[],[],[],[],[561],[],[],[678],[],[],[],[],[778],[],[678],[],[],[],[],[],[],[],[952],[278],[],[],[],[359],[438],[],[],[],[123],[179],[874],[608],[],[],[919],[],[],[],[575],[123],[],[],[],[844],[],[],[],[],[721],[],[],[678],[36],[65],[645],[],[558],[],[],[],[6],[186],[246],[610],[80],[],[],[],[265],[],[287],[18],[702],[0],[],[349],[],[],[855],[],[],[],[430],[85],[212],[],[],[],[],[464],[],[],[659],[],[],[],[652],[],[283],[],[],[562],[],[713],[],[],[],[],[445],[],[102],[],[],[],[],[],[],[399],[],[22],[91],[],[750],[],[],[],[127],[],[],[],[],[849],[400],[649],[],[438],[],[],[],[],[],[17],[],[],[],[],[516],[],[],[],[],[],[80],[945],[802],[401],[681],[],[],[682],[680],[906],[],[236],[],[],[676],[974],[],[],[],[],[],[],[],[],[101],[],[],[],[],[],[349],[],[],[],[],[],[],[98],[429],[222],[],[],[],[],[],[],[109],[],[248],[],[],[],[],[897],[290],[],[977],[],[],[467],[],[134],[461],[],[],[],[],[],[71],[],[480],[791],[921],[16],[938],[],[289],[],[],[611],[52],[],[98],[559],[],[373],[],[],[],[115],[],[],[],[],[168],[],[817],[],[512],[310],[],[],[],[124],[],[],[],[],[552],[324],[472],[],[],[],[468],[],[548],[],[],[],[],[],[],[723],[],[],[],[],[],[579],[507],[],[703],[],[288],[],[],[],[],[818],[],[],[],[714],[],[],[],[],[635],[],[],[],[],[564],[],[895],[861],[],[499],[],[],[],[],[507],[],[769],[],[],[600],[571],[],[],[269],[],[],[],[],[805],[],[],[],[],[351],[],[57],[],[],[],[],[598],[],[842],[],[],[51],[73],[],[],[],[459],[],[],[764],[724],[],[],[],[609],[328],[],[230],[],[],[],[],[849],[],[15],[],[313],[],[513],[],[],[],[],[492],[],[],[],[],[],[],[],[425],[],[],[360],[945],[],[714],[],[],[],[],[905],[655],[],[],[767],[394],[582],[],[],[],[997],[736],[],[42],[640],[],[],[],[724],[791],[],[311],[],[],[],[],[285],[452],[563],[],[99],[],[],[],[857],[535],[],[],[],[],[],[],[431],[],[],[935],[],[],[721],[651],[738],[687],[229],[565],[],[],[],[],[],[],[683],[],[],[],[],[],[640],[0],[32],[258],[515],[],[652],[],[],[666],[875],[149],[808],[],[],[],[681],[],[799],[],[],[],[955],[],[509],[],[],[],[201],[],[],[],[],[99],[],[],[],[],[],[],[763],[],[],[],[113],[],[],[340],[127],[],[],[],[837],[],[268],[],[710],[],[],[],[893],[134],[672],[],[853],[],[],[],[788],[778],[],[],[],[],[775],[],[],[],[],[230],[68],[],[],[297],[],[],[],[],[],[],[],[],[],[],[],[],[211],[],[691],[675],[],[],[858],[],[701],[],[],[],[910],[108],[],[885],[],[],[],[411],[515],[290],[],[],[],[],[],[681],[660],[567],[],[],[],[711],[],[],[818],[479],[],[],[],[861],[772],[26],[714],[],[],[],[],[779],[],[940],[887],[],[25],[],[],[595],[],[],[986],[],[607],[784],[],[842],[248],[120],[],[218],[],[82],[],[695],[],[],[],[3],[414],[],[872],[345],[],[],[],[12],[],[],[618],[],[],[],[],[573],[323],[],[517],[],[699],[],[463],[53],[],[455],[716],[261],[],[],[945],[],[],[],[159],[],[],[],[],[911],[756],[],[],[],[],[],[],[],[],[],[],[370],[],[],[901],[202],[458],[443],[421],[],[],[684],[828],[720],[973],[65],[],[],[],[238],[151],[496],[507],[],[820],[971],[],[],[9],[],[],[],[],[],[544],[],[],[],[],[],[471],[],[],[345],[870],[],[],[],[372],[],[],[],[267],[803],[701],[300],[],[224],[],[],[],[699],[],[],[],[187],[],[235],[],[],[70],[],[],[],[616],[551],[],[],[317],[797],[],[77],[966],[686],[],[],[],[],[],[640],[],[],[35],[]]
        exptected = [None,True,True,False,True,True,28,True,True,28,True,True,True,703,True,True,678,678,34,34,True,True,True,703,True,935,True,935,935,True,True,True,True,28,True,105,105,True,28,28,False,65,65,True,True,False,420,65,65,False,65,True,True,False,True,True,True,True,False,421,True,813,True,True,28,835,835,False,False,True,True,True,686,860,False,True,991,True,79,True,930,930,991,930,True,True,True,True,True,759,759,759,True,False,759,False,True,True,746,True,True,746,930,True,951,930,930,930,True,True,False,True,True,False,True,False,930,True,True,79,True,True,772,True,772,True,315,686,315,686,True,908,True,True,False,772,772,271,False,True,True,True,False,True,593,806,593,True,True,True,True,806,806,806,True,411,411,501,501,True,True,64,806,806,True,True,True,True,391,391,True,391,593,True,593,171,171,True,False,True,315,False,True,742,True,227,True,True,845,True,668,668,668,True,False,True,True,171,True,True,True,True,293,True,True,True,65,220,True,False,False,True,643,643,True,True,781,781,False,909,False,True,909,False,True,909,True,561,909,True,909,True,678,678,778,778,678,778,678,True,True,False,True,952,True,True,359,False,True,True,True,True,True,608,True,True,123,False,123,True,True,123,123,123,True,True,123,True,359,True,721,721,True,True,True,True,65,True,558,558,65,True,True,True,True,True,80,True,True,True,True,True,True,True,True,True,True,False,0,True,True,855,855,True,True,True,85,85,212,85,True,212,464,True,659,212,659,True,True,True,283,283,True,562,True,713,True,283,True,True,445,True,False,102,659,True,102,102,True,False,True,True,22,True,91,91,91,True,750,True,False,False,True,True,True,False,True,438,True,True,438,False,True,17,False,17,438,True,516,438,438,438,True,True,True,True,True,True,True,945,True,True,True,680,True,True,680,True,True,True,676,906,906,676,676,676,676,True,101,True,906,676,676,True,676,True,True,680,False,680,True,True,True,222,True,False,98,98,222,True,True,True,98,True,222,True,True,True,897,True,897,977,True,977,True,True,False,461,True,461,True,True,134,True,True,True,True,True,16,True,False,289,True,True,True,True,True,52,True,True,559,False,True,True,True,938,True,True,480,True,False,True,True,310,310,512,True,True,310,512,True,True,True,True,480,True,False,True,472,True,548,468,548,548,468,468,True,False,723,False,723,False,True,True,723,True,703,True,False,507,507,507,True,818,507,True,True,714,714,288,714,True,635,288,635,True,True,True,True,True,861,True,499,499,499,499,True,499,True,769,769,True,True,True,600,True,499,True,499,False,True,499,False,805,499,True,351,True,499,57,True,351,True,True,True,842,842,True,True,51,False,73,True,459,False,True,True,False,724,764,True,True,764,True,True,False,230,459,True,849,True,459,True,313,True,313,313,313,True,True,15,15,True,492,492,849,True,True,513,425,True,True,425,True,425,False,714,425,True,True,905,True,True,True,True,582,767,582,True,True,736,True,True,True,997,640,True,True,True,True,640,311,311,640,True,True,True,True,True,False,99,563,True,True,True,535,535,563,535,535,True,False,False,True,True,True,True,True,True,True,True,True,565,565,True,229,False,True,True,683,True,True,683,683,True,True,True,True,True,True,True,515,True,True,True,True,True,149,149,True,True,False,True,799,681,681,True,955,True,True,True,False,True,201,True,875,False,True,99,99,True,False,201,875,True,763,True,875,True,201,201,True,True,127,127,127,True,True,True,False,True,True,340,268,True,True,True,672,True,853,True,True,True,True,True,268,True,778,True,775,False,True,True,True,True,False,230,True,297,230,False,230,230,297,False,230,297,230,False,230,True,False,True,True,691,675,True,858,True,701,675,False,True,True,108,True,910,910,910,True,True,True,290,290,290,515,515,True,True,True,567,681,681,True,681,711,True,True,818,479,479,True,True,True,True,26,False,714,False,True,True,True,True,887,True,25,940,True,True,887,True,True,True,True,True,True,True,True,True,True,True,True,218,True,True,True,986,True,True,986,True,True,False,872,345,True,12,False,True,12,False,False,True,True,True,323,True,573,True,False,True,True,463,True,True,True,False,261,True,716,945,945,True,945,945,True,159,True,True,False,756,False,261,True,911,911,911,False,261,True,261,370,True,True,True,True,True,421,458,True,True,True,True,True,65,973,973,True,True,True,True,True,True,True,False,151,True,True,True,True,496,496,True,544,544,False,False,151,True,False,544,True,True,870,870,870,True,True,False,372,True,True,True,True,300,True,224,224,267,True,699,699,267,True,267,True,False,187,True,False,70,70,True,True,551,False,True,True,317,True,True,True,686,True,797,797,True,True,False,False,True,True]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(exptected,outputs)
