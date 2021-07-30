import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/bitwise-ors-of-subarrays/discuss/165859/C%2B%2B-O(kN)-solution
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        curr={}
        sett=set()
        for x in arr:
            new_cur=set()
            for y in curr:
                new_cur.add(x|y)
            new_cur.add(x)
            curr=new_cur
            # for z in new_cur: print(bin(z)[2:],end='  ')
            # print()
            sett.update(curr)
        return len(sett)
class Solution2:
    # tle
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ENOUGH=32
        def add(a:List[int],b:List[int])-> List[int]:
            res=[0]*ENOUGH
            for i in range(ENOUGH):
                res[i]=a[i]+b[i]
            return res
        def subtract(a:List[int],b:List[int])-> List[int]:
            res=[0]*ENOUGH
            for i in range(ENOUGH):
                res[i]=a[i]-b[i]
            return res
        def bin_to_int(a:List[int])->int:
            res=[]
            for i in range(ENOUGH):
                if a[i]>=1:res.append('1')
                else: res.append('0')
            res = ''.join(res)
            return int(res,2)
        def int_to_binary_array(a:int)->List[int]:
            binary = bin(a)[2:]
            binary = list(map(int,binary))
            binary = [0]*(ENOUGH-len(binary)) + binary
            return binary

        binaries = [int_to_binary_array(a) for a in arr]
        pre_or = list(itertools.accumulate(binaries,add))
        res={a for a in arr}
        for r in range(len(arr)):
            for l in range(r):
                tmp = add(subtract(pre_or[r],pre_or[l]),binaries[l])
                res.add(bin_to_int(tmp))
        return len(res)


class MyTestCase(unittest.TestCase):
    def testVisual(self):
        arr = [1,3,4,6,7]
        Output= 5
        self.assertEqual(Output,get_sol().subarrayBitwiseORs(arr))
    def test1(self):
        arr = [0]
        Output= 1
        self.assertEqual(Output,get_sol().subarrayBitwiseORs(arr))
    def test2(self):
        arr = [1,1,2]
        Output= 3
        self.assertEqual(Output,get_sol().subarrayBitwiseORs(arr))
    def test3(self):
        arr = [1,2,4]
        Output= 6
        self.assertEqual(Output,get_sol().subarrayBitwiseORs(arr))
    def test4(self):
        arr = [5,18,11,56,27]
        Output= 9
        self.assertEqual(Output,get_sol().subarrayBitwiseORs(arr))
    def test5(self):
        arr = [516687396,389879643,590163364,571461338,504752889,67969721,217118278,978097830,607688973,580245686,581899856,818996193,290536372,55567837,380618960,959442844,120068378,731357054,902134578,672169978,860162318,272900210,939081068,365489612,319122438,389535653,282445195,831361610,286528234,282908985,345559894,289734598,851444213,120230293,204759039,223643194,463792866,889953524,526850329,108343187,998204566,463944195,932416542,701659579,575904119,159565286,175723846,940549369,780025489,251736859,71347038,317149441,929543627,439972667,696709457,555659462,494202109,556010280,414347482,736792470,416171644,952541362,224487419,260241579,429814994,372239248,79447033,215787157,49336399,413679799,635544494,85670753,606468682,586702863,252046193,554791864,676460965,731516855,506718759,480825569,720664762,943285595,979735620,897900549,917703562,422020756,642597405,405636398,298790114,142710797,147392138,241986215,137972541,302524733,256546068,687908719,772987378,314748241,147714978,929378950,140365536,951143862,83251284,754223333,938780828,563136060,748441889,804856126,85983304,851952684,515834148,671599070,839169666,196929029,975103091,227919845,829776456,854471045,157102578,638566075,184849791,843430296,94255464,561962765,85774175,953012204,624208564,156456170,573691325,423756270,215158687,251015851,411981367,331716436,274225902,696493080,730125320,954086414,82636791,469020944,322808269,574196160,151886277,239678581,321962271,643227895,903310561,609038939,639912222,711485794,995401591,37341370,326113894,755841995,974185422,211330378,989748643,820815281,768276368,4299900,452418663,914515324,229195038,944833690,66015939,918197627,738510892,150284561,641235328,518238457,9994892,482729702,190677182,228754830,779365360,443609467,288919612,715331900,133584395,244532930,809499242,365286353,810337484,563131653,35562786,73642957,130580572,810107922,321910658,233976759,453300408,304110055,271556318,77570307,222670501,770035791,590906042,678087503,856935054,3619071,964229401,191185533,761914873,648831043,328695876,280608005,698141112,19361633,914750422,906810152,126939986,213370210,520192974,715181450,922294112,170613897,417511517,569748343,192758539,639362675,153133280,147817992,117351804,275198356,930809490,410352357,663897300,661021734,391399068,430332079,801590669,89445473,726096603,50745999,859808559,755986747,787422264,559365864,777038783,903736232,536979935,202206991,613914611,447161441,597285817,764554188,586560160,404421330,234801345,529237904,684226180,565804615,528549909,198293278,769208871,238158976,721378690,876875866,832698370,595598512,628511568,248151502,925732108,222632552,651228356,257808473,425321955,924673960,571219636,216842788,809845976,69280431,284986389,844787083,356295414,477694956,637783448,806550197,280481012,386182759,251852013,978546725,938472413,983501543,121144189,868268289,743053532,377192224,531759347,53237056,66163849,64506801,71103048,720937049,83098105,984306449,111103039,717169585,90581161,905425625,16102368,851228927,86479837,969972529,161625175,786631883,499438647,929914086,960039820,690443705,478793063,19294825,682332496,837520995,272501751,124590861,904109253,738393452,68393464,462261204,409826045,101496490,582666357,530428788,456145868,343349235,976487340,643759255,616853125,698829796,613612280,416777431,269284803,526316969,247490319,557345415,655783673,562190709,223705132,97422976,526791194,90633826,398673055,337913750,31909869,208671899,306302953,896961989,279297970,348513784,998806648,956796672,312521377,393294369,542452286,166676608,400618150,519088887,652899234,361964135,822603908,988863511,654308943,928448947,290207020,216646153,375821258,115856708,730696356,886727417,475084310,853959483,562383676,458840021,862301261,555250448,497562429,177387057,159570005,180162802,853652965,838733356,308925158,71261657,43107585,653679276,42087060,293076617,610632035,628723951,687413376,877960821,602393234,8540101,871513168,165742209,216988241,622091663,984611683,218053334,377497867,706360902,29502636,507837557,992175680,115575355,804731245,403043531,228954802,385934278,141927252,427387513,493104933,923446061,567066387,915633750,65576820,584214665,841245242,407612493,525969158,176125530,24276825,890677283,503328967,415369042,180771929,132748618,378127239,920375850,45976116,590902041,255547963,697270098,934897645,638113190,554008374,838951663,824611412,305651816,810280853,462514724,45950911,199997942,429437095,39769604,563224274,322390458,797932455,325559652,44512760,826632472,132477967,788884401,698097251,869586672,695402384,477042266,377735564,627863696,462263024,551237949,792978910,673706859,423794592,218529320,371587240,383897099,346721998,858232322,676202035,320150548,349690859,805364424,497716924,117648306,841449869,468924531,634067524,739612906,943923996,954527745,888205231,797361281,862030795,412692829,965817896,812116530,561196206,102308502,968534045,558720180,974566067,299836828,284095176,815142497,206888491,854518062,240651975,172347305,615033508,433023499,823751447,628318121,519074580,251497485,235355447,449206997,795306774,489139787,856213918,234055793,874730959,827219794,970832973,588622476,720434733,194829168,596202465,469696428,92323557,740148395,980426911,759054944,745599881,820573882,239100225,657857416,330348480,420153975,661907783,501133475,851997282,175062034,966056109,689671689,934136842,316370148,466054963,354388992,334763162,845271456,824466014,589298015,372111153,544080704,795844025,666587956,432808521,583751253,234121317,170599628,185739418,491484477,121508156,370096486,557868106,655472340,599895396,964941505,48594557,405199300,54135555,985218114,77072899,641125049,956212492,154378143,863377181,319146426,276639778,67669072,795264161,492181086,574179698,545828544,238137704,313244512,73789707,308568588,677701733,53473241,718648130,808533256,112588251,293018479,463025033,83142367,292052375,174542716,642292364,63245082,672196879,583252240,764044055,184876127,30184181,84765724,628008031,611403497,907405233,406144259,525278021,687640769,929147960,262454440,976814924,580300216,975744695,767896802,69562254,514476631,545709939,965241889,525993337,783766343,139477245,360916885,486524375,377678788,42931947,902400576,844365837,622048979,500680979,75119846,700163685,239721556,558606413,507722492,618341329,494490144,600422621,655244508,173591313,179099458,451372543,603946639,69089456,657673808,235212130,400217264,232354316,339451885,279473233,793338197,160155020,756582596,610951545,639976010,683391005,285711627,291913482,67717233,275323180,513780506,943981631,695860346,368337097,10010796,368176805,733727622,334302126,258763759,803310793,186876755,303276464,671970996,574145276,386329544,769554357,727699938,735486241,412391258,765299652,802030993,128116070,232311312,962884631,59694111,980422456,487755495,178418783,843229535,500426391,405861536,993838012,975497076,58899691,18508013,909305434,746401982,60545835,473069617,89045212,584808966,76411914,469570129,574180106,789882848,56114666,926953813,561650488,701500815,84112190,512253500,41550888,275837376,22016677,518546880,429295518,644374172,34077823,878030262,700396298,59062089,874875906,357047492,21687153,84974584,6749088,108902521,487929337,939135653,227025733,649499059,33009732,445665170,710043114,911624338,994380363,474940573,574877796,957333932,312501641,254077496,801273830,249198504,758462338,982045057,984341924,345972014,179786806,175624918,494546640,376766368,270651562,983165417,874556316,129492552,796827057,134296633,425694705,508246460,63954892,194897486,422572346,347126919,3836874,869791445,645805142,10469746,106603189,217552224,264947188,32316748,310261137,302269776,42867711,306435046,576576477,975354970,361733321,926384821,888443633,965777628,492782302,595195192,153477857,770660124,767611053,303063299,449352962,715725169,340222418,546876335,563943323,677711544,775008358,248669410,39160206,725538025,785142742,781522347,886614663,566419294,866997945,465661738,274075703,356276009,278570937,119433936,490870422,531625842,637045499,742638918,891131782,541781157,98128639,239582636,168333424,294847790,465028887,284401893,199758150,643934986,537349861,693316887,739879097,452176411,671682343,458001842,82214530,519145902,500106699,659616222,716034094,953513531,682289718,941471750,203349475,670427718,958018823,880681823,801842519,188420050,43248317,617842758,293759344,823556910,883210515,177977799,868899969,992958616,497951886,628228533,345547385,218065473,698536599,967289037,110539543,452086210,59552028,313740728,407654831,622063782,189847547,636150692,87599214,761335391,843630496,287566137,394942638,565505524,50336879,53491633,928796606,600358761,812956731,713104910,902339148,863296559,455257450,4858197,807888617,806699419,581281781,551708785,671637499,312862999,55467278,217768337,866474401,744232218,710796981,279917682,589426715,983345198,103437374,211436525,586112330,803907394,706838122,755706242,217100176,181822975,101445352,678208274,203223830,785128903,624347827,809819127,291659175,601555168,3887186,972528548,534526876,378418012,10772167,920198369,743465926,913283129,86630273,710819084,543451136,980332185,696336459,462790447,430931,543338991,306366675,311346385,426099754,548130967,918779180,37676326,577943708,923377344,324147538,909097034,42290522,569721629,926897792,524623579,658925928,4675552,385066447,326623972,102619814,341772539,493777718,627013663,164112326,760251920,476750371,204180718,813134165,360109429,629205441,175066991,292598841,546385683,681285470,707519555,457590943,411474499,595811561,977944811,592343392,7302543,829851955,967721795,588485218,234447649,743246333,996227604,542132270,431108959,495702917,544595036,97799173,780970429,977163375,31921665,531121522,651191070,854217372,691979420,851611986,137473488,706022425,457707115,47834439,962682008,992727292,205688646,223440527,180726614,660855024,418430061,458311122,779526798,365067788,510257349,343690378,944461970,987855282,743288751,497819382,71152239]
        Output= 3295
        self.assertEqual(Output,get_sol().subarrayBitwiseORs(arr))
