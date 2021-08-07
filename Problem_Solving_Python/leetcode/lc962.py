import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/maximum-width-ramp/discuss/208348/JavaC%2B%2BPython-O(N)-Using-Stack
    # https://leetcode.com/problems/maximum-width-ramp/discuss/208348/JavaC++Python-O(N)-Using-Stack/211767
    # time O(n) space O(n)
    def maxWidthRamp(self, A):
        n=len(A)
        maxx=0
        st=[] # decreasing stack
        for i in range(n):
            if not st or A[i]<A[st[-1]]:
                st.append(i)
        for i in range(n-1,-1,-1):
            while st and A[i]>=A[st[-1]]:
                maxx=max(maxx,i-st.pop())
        return maxx
class Solution2:
    # https://leetcode.com/problems/maximum-width-ramp/discuss/208348/JavaC%2B%2BPython-O(N)-Using-Stack
    # time O(nlogn) space O(n)
    def maxWidthRamp(self, A):
        n=len(A)
        st=[] # increasing stack
        indices =[] # corresponding indices of the stack
        maxx=0
        for i in range(n-1,-1,-1):
            if not st or st[-1]<A[i]:
                st.append(A[i])
                indices.append(i)
            else:
                fake_idx = bisect_left(st,A[i])
                real_idx = indices[fake_idx]
                maxx=max(maxx,real_idx-i)
        return maxx
class tester(unittest.TestCase):
    def test_1(self):
        nums = [6,0,8,2,1,5]
        Output= 4
        self.assertEqual(Output, get_sol().maxWidthRamp(nums))
    def test_2(self):
        nums = [9,8,1,0,1,9,4,0,4,1]
        Output= 7
        self.assertEqual(Output, get_sol().maxWidthRamp(nums))
    def test_3(self):
        nums = [15942,40892,41699,45505,27967,40539,49295,35491,48517,23679,49477,37060,43788,31154,28806,4935,14039,15785,22669,30410,32062,6359,11122,48286,37242,46469,39151,1124,46961,21274,38107,25720,11908,41761,17900,43096,17312,26848,36833,11535,30788,19062,43410,44667,29854,21067,49178,49276,12599,40021,34135,21991,48531,21963,9411,37687,7005,20588,28096,10057,49608,26886,30057,39133,9582,25694,45599,21890,13618,9348,26792,41202,31836,42225,33105,40869,25666,38304,31852,6049,36378,2987,22957,33937,10205,12792,32204,20500,14851,14746,46850,17225,47883,17357,21851,14468,28636,647,37545,10334,47310,34166,42452,18789,41366,49366,27939,40991,29460,40757,445,13370,33771,45340,11127,2217,28416,31797,27126,47072,18861,16559,12335,5634,41023,31572,46016,6718,7441,6703,39962,15364,923,31260,7787,48828,22464,30548,44703,6948,40287,4197,49214,29177,40363,36185,33163,4870,7519,20368,11248,41158,41673,42318,34481,49894,48856,45759,30501,14543,739,6182,10302,30633,10829,20190,9883,13371,31239,4686,37019,4482,25478,9080,30125,12316,13230,19960,45782,27295,35388,38321,2244,28876,34112,16870,4988,44434,41950,33255,49029,41979,48824,47763,26267,49563,13027,31853,12953,28880,24503,22163,14766,44848,43361,3528,37392,26612,49352,37126,38715,36735,31263,35663,43747,45087,46348,40797,39868,21078,12865,34450,18012,48796,30745,49092,15546,13833,35678,48044,22597,45789,12203,20643,24906,11249,41755,14244,49328,46537,46623,18212,19302,45760,44162,36259,17451,42544,47438,45425,14804,35253,37377,49341,28443,30561,43805,23968,1203,46451,41641,28482,4999,23714,12762,44162,47285,32261,15997,27476,24755,34323,4165,37843,397,39894,33697,17131,1096,39460,34219,10213,36274,8213,5356,6940,44206,4146,8877,40437,8679,19161,14852,4718,3127,16993,18276,25938,43054,31371,13962,20201,12907,35473,10068,10328,49384,30016,22187,19170,44107,20658,44117,1173,12427,39491,2630,10990,27218,33383,21249,3761,48397,8937,13448,33648,13173,9815,39662,7495,5790,13087,12217,33520,9178,6989,9798,29698,19405,30784,30748,33853,14322,43787,33314,45461,44035,13655,40406,42825,19867,45220,7550,25332,34387,11118,14589,28055,15171,29143,28511,49320,27569,39405,9509,940,49835,9737,14779,49095,45348,32649,14748,2942,21332,36580,32819,23923,35201,21196,8083,9017,32577,13500,49732,2963,6504,845,40028,44294,34839,27908,47776,11739,22314,3630,29963,17789,44749,9753,36414,32798,43707,26801,8538,26465,40655,23000,23468,27807,42002,48239,27676,40567,3624,10278,15073,17455,33327,47335,880,48725,30801,49913,11199,27382,23041,37052,3971,33284,14412,9875,1823,41362,15320,39075,30315,1967,28128,10495,6086,10178,19555,46075,27803,31417,3541,35821,38106,45461,13481,17242,29837,20760,38545,43556,38912,37772,12495,2400,22006,224,27955,18364,13716,796,8716,42360,33932,45116,44436,17496,27079,40101,7522,48521,23996,8865,13235,5773,41433,47656,21874,29807,48336,7850,39683,27742,2514,48703,37722,12636,23553,17784,39634,14396,26991,20699,28473,10732,15673,25870,34007,1799,27264,9634,39745,4968,39897,9753,44917,39721,7772,49583,10593,45544,16790,12023,30370,2538,38662,22493,28525,44049,27351,34792,27446,47161,49297,26612,40656,34198,7371,29980,30082,13153,18168,34926,17163,27578,19826,21472,37493,24845,9659,6534,45747,27006,3049,35179,34540,13205,41242,5593,30500,37087,32291,10528,19628,20906,13747,20529,20090,45958,2349,39111,20717,38745,40680,13350,25190,31665,655,29662,20709,37924,34203,102,1622,15186,42694,8037,6004,13389,7102,34658,8805,43057,34170,26349,9705,49223,21530,40596,42372,16900,25729,27253,34157,25031,46730,26516,1718,46035,36219,24153,35656,25115,691,9381,46202,10396,15417,43087,46607,8312,4761,5959,32744,16229,8306,36609,34789,8652,48797,14586,14242,27140,38333,225,46201,12645,31112,20763,34036,42372,25172,46064,1662,11299,2904,38395,5393,21041,38914,45049,18928,16722,169,44751,28239,26482,45320,35071,46386,30457,41423,28141,41672,40053,30899,47484,42904,31352,37305,3274,32775,44377,39400,20771,24409,33028,2766,22627,7679,15874,22762,19279,6561,35363,6093,24636,40476,25712,24429,15831,10967,35830,46799,28638,7901,32264,4674,7558,42337,1815,30081,26219,7722,43290,26327,3505,42512,46444,23137,5623,23577,42949,43286,49687,14310,36426,11567,41482,48465,11974,29206,32682,8699,46546,13733,30570,40984,26571,42410,16726,18669,48305,27634,24719,7880,46550,10516,34697,45642,6238,46837,16099,9965,3859,30136,13124,14293,26109,49646,9131,47145,44156,37910,29048,46149,36051,44090,10965,5692,25331,36688,5938,18366,20528,23073,45047,6428,2201,43729,14824,20141,41162,8835,24108,39493,35164,48939,5567,27125,25003,37402,14761,48292,33156,49183,7216,44912,21965,11589,25611,48211,10194,26048,4706,21566,29813,21731,48571,40998,14937,24804,2860,28530,9211,1424,23671,49967,19548,46954,29414,36918,27134,33601,41636,4718,35993,31238,35078,36099,769,41942,29635,31302,11635,26144,5248,34424,43924,38944,33402,25653,29651,16627,47143,27340,23163,28795,42118,31600,10686,18709,27770,38730,30738,30365,15171,48607,21756,4624,37920,26371,3390,20565,11304,9041,17997,34777,48226,18069,3167,9256,22268,23969,8971,14827,29621,30698,6976,46924,34918,20371,12312,36148,17121,10600,34431,27812,34987,11733,24211,41474,16005,41761,42615,48322,34749,30054,14703,42896,23468,45656,49047,35239,34775,7992,2271,31864,15963,39720,30905,35670,22935,35955,26148,36578,20059,23604,44845,29223,34721,30470,3153,24989,44252,2456,44915,29757,14500,45845,47960,34620,30810,37787,12157,8893,3724,35923,49588,20775,43928,46862,35272,11544,36887,29138,26256,43831,35201,10164,39982,11209,44312,28318,25865,14846,17871,40105,35637,41479,6675,20733,14606,44532,44381,34821,19109,31926,38899,36597,9332,43029,28607,47404,36274,11102,13272,4594,31629,41795,16730,11290,5849,31148,10430,47683,13016,13841,5330,36443,42943,38255,27453,24691,31298,21615,7415,1788,13853,3096,8868,46771,37141,5070,37207,4822,9442,28525,22799,48614,38217,17724,13328,39703,43262,44098,27414,49156,2796,39290,21658,34302,12266,12762,7181,45606,16657,29334,46923,43419,8000,38568,2436,23564,46992,35130,46829,9879,48536,43523,5741,31782,2353,8345,14987,5582,38181,38663,39927,31836,8671,1948,41369,13190,3890,22850,2306,4947,30699,32472,19712,32490,17573,37633,16743,28105,4781,33739,35992,42256,11472,4903,19778,1886,14256,6750,30101,9872,21589,47949,37669,9669,42259,32105,33045,43425,42570,14923,2117,1666,41400,13212,24742,487,6124,25839,17067,3602,34919,6674,24116,20316,9288,45098,17281,5992,7365,39629,41950,5713,19461,7208,25362,8993,27653,42261,27506,23032,25974,8217,4157,10182,43762,32821,42871,16863,4238,19313,29241,47755,17732,16653,17129,35099,48458,22734,46111,5765,10386,4595,39477,36275,1642,34434,48648,17603,2463,43345,20288,31699,13904,35230,25308,45820,44443,32538,11277,39015,5362,25282,1611,27150,11631,33902,28590,6841,25702,13701,18347,21671,20876,25662,36968,32083,11465,4060,3259,10921,14422,30744,6045,12519,23721,38409,24219,37664,29071,7172,47389,27060,33149,27887,47394,2559,11834,49977,44463,48947,42604,7721,26917,24645,48528,47746,8042,31364,32193,8195,28104,14482,13258,20426,42980,42818,105,39681,44076,15656,2227,26832,32054,15762,39929,34474,10891,49428,44280,6393,49719,30095,24669,49809,36663,34814,26777,40212,27488,11587,3178,30700,40314,36249,22481,43434,29971,16067,30797,22151,15347,42675,15122,5871,8398,32199,3052,30467,8224,44176,30508,1489,38854,20195,47925,119,26669,6128,328,31341,8192,379,34342,42040,2670,35127,23538,23003,27481,43225,5019,42130,4446,27053,44649,44165,33163,49662,46547,17826,46100,14881,25406,18493,36323,12870,26207,25990,32903,42957,11955,13960,20282,10814,34387,8293,34239,39887,11592,32451,13815,17856,13038,19595,43962,32643,46796,6419,21161,22030,13826,23889,36525,45223,31974,46844,39377,49051,30181,19533,2977,20501,15704,9209,10641,18612,19963,8882,35355,49109,377,4093,44285,15171,28320,47326,16376,26887,2236,15713,40496,9555,32377,49688,38876,29468,39759,904,36476,47077,38383,47483,32002,13361,10826,39764,7943,6084,16339,38213,12232,27974,41569,23111,27194,17573,35894,11324,13157,13760,19238,9163,46984,26352,35167,15050,33989,11353,25193,41887,25423,38335,48465,36191,20798,26908,10273,43722,7457,17965,33923,37327,3759,29971,35430,11227,44453,27509,3623,47479,5400,36040,33258,23380,35125,45981,10864,41148,32971,17631,7766,13147,8355,46201,27412,21772,37906,11858,34726,17643,30809,9992,24189,1746,16405,20760,21860,46367,15695,40784,3093,44019,22654,1740,46409,37504,27323,31159,1601,16475,27913,46219,25522,15170,41796,22989,24954,13689,7346,40826,40513,24694,46884,26262,43797,35514,41072,11805,11166,16458,41532,17018,8203,2339,20983,29809,5216,32725,49820,2881,16027,30926,18471,34045,21931,45673,43746,29800,46909,37211,9787,320,13903,42590,2419,25687,39247,45878,12945,17053,47213,12909,31441,1826,7362,4484,17805,39751,15036,21774,4848,42404,42786,33422,7238,33824,18019,10912,4929,42583,43218,10146,22276,33484,3649,14360,27173,36486,614,41290,49069,27396,46663,32842,4926,3113,18218,1025,26475,2603,17968,12444,19569,12981,45657,35830,46678,18233,42463,15276,40590,21694,5166,29873,41931,23678,27343,9298,29204,31090,42167,11965,33291,40494,44377,9334,30426,21371,34725,516,22725,43104,14188,40426,28521,29673,49258,33160,8461,3446,19008,7675,1450,24904,28600,15153,34188,718,8998,29281,2673,45281,26217,29070,6171,9733,33836,10175,12093,16336,1491,36152,40429,41208,2338,13200,10549,46409,20509,45582,45639,41900,23,8602,42697,32490,40024,46405,39508,4476,45569,42613,14094,45389,3575,39844,28008,35898,14444,37876,41993,10542,26204,39542,676,9748,36116,32711,21514,22009,1846,32559,10406,32261,42407,21192,13455,28532,5793,26248,46523,35018,1950,39867,39695,36526,36908,39984,7296,18663,48594,28883,7082,14078,23283,41210,30100,231,9690,39581,7813,38724,11641,17756,46548,17979,44822,27931,18870,1099,22828,23880,16722,32122,42427,31966,40294,12476,25196,29576,26042,40505,11049,1535,49945,37079,43847,41305,32857,32641,24955,46939,27834,13280,24619,22593,1651,6619,31297,5281,13188,9605,7355,14344,43332,11538,42485,45499,3281,20776,43184,39415,49698,36216,28477,33675,6570,36928,43029,36792,15828,19685,3700,29336,36799,14026,48877,34349,29189,35328,32256,1083,25793,31823,20098,2678,10649,12582,37779,4871,2531,16864,16365,49229,11058,10654,49870,9818,26697,4402,856,39944,9528,10508,101,44831,33401,36391,4889,2307,6562,49489,13815,40962,27814,13370,34935,41901,41186,23095,36843,5477,3131,16083,42255,41723,39580,7463,2196,7600,37758,19406,16109,26560,42273,46540,48605,2407,25463,19298,6018,20047,9462,18281,47895,34964,8563,20870,12604,916,25923,33801,15833,8778,9847,48017,203,24218,36020,12293,27170,19232,17597,32451,5022,20753,34607,5621,35071,24373,49771,13278,13455,3647,20799,8261,81,14967,28381,18322,796,22967,25092,2295,3835,40398,22812,21801,34248,35305,42935,14780,42696,45769,48971,1165,34562,21565,9874,20249,45047,14285,14507,28852,11554,29460,20526,32535,13012,8411,5440,16286,41217,4895,21052,45980,24846,6507,7296,2216,11709,9613,10623,13000,8666,24780,11370,8125,18038,22422,2333,33971,8586,16622,31788,43880,43516,30942,45304,13569,19785,16211,5477,8360,35366,34133,38260,34661,44925,45570,28229,9924,47204,28063,15836,36594,34032,21263,10970,26678,8526,9326,25178,11948,40832,26595,26077,3817,47712,4234,20259,22618,37410,24655,11928,19354,25547,19793,7591,40360,29391,44767,11015,27395,1915,5889,24127,6465,19857,7284,18776,14157,47007,23601,42536,34319,24240,20488,46600,2993,22853,46260,45384,16915,22300,17397,25059,20266,8262,38366,35614,33660,17843,8607,9414,5035,31059,6174,36991,9096,25656,15186,42562,28955,13567,21734,19026,10319,30523,7241,26427,47803,2042,41534,44144,2005,49414,26560,11532,30680,18376,6947,43242,30027,9782,2753,29240,25081,24300,24985,20573,25369,22172,49175,18409,25921,5739,35016,39508,41661,9884,34805,17195,35964,18417,9812,9266,49324,17830,5046,38455,7128,36014,18012,6853,33426,38161,4175,39142,29379,378,30887,21569,33035,31255,17521,10317,36349,45378,27042,45444,20278,9264,5993,44857,36174,12314,30858,25151,29723,38008,34606,39434,32373,17229,42383,11870,47658,46154,34588,6108,41800,35038,37244,23307,22961,30581,38209,27851,19016,11229,2353,7806,38500,38236,35926,9964,17060,22300,25146,2023,42300,25292,40546,32714,45772,26680,31826,23743,43923,3382,45865,4246,33420,5885,17977,40740,6364,42987,220,21164,10101,29279,9908,6189,16003,17911,34343,12486,20124,1471,40200,30047,6300,25992,35385,10705,2936,9339,1564,39384,29723,26035,10523,49392,35742,2328,43218,43041,38439,33628,32809,47143,47927,10251,31024,22508,43029,21101,18700,3015,10911,1691,44555,24606,35375,30885,31776,23485,3104,26223,42738,36403,39515,18901,33172,7806,5172,19876,13014,16007,6015,6507,46338,33145,47339,34770,47217,27574,33127,30029,26816,28882,6716,21848,19790,27828,32705,46496,18261,35259,46837,42714,26120,13241,13351,15622,776,24750,40603,37566,16832,32663,3956,39602,48838,18633,11631,34066,36077,46041,25199,35291,45144,15053,7319,9083,45966,7663,45306,4174,4068,38596,46122,28379,48406,45816,6043,40368,1794,46584,16320,10657,29614,7879,43658,44414,2235,4269,23083,22785,37590,17906,26060,37901,30650,461,21995,41593,43394,35982,49351,21322,18299,16217,18886,36352,11425,45476,39571,3823,19385,9149,23057,23403,4625,28705,2318,1603,31370,1264,48704,14302,35505,45607,19800,23675,24734,39832,30506,41300,48614,26635,4649,23994,31805,42481,30505,27849,12410,48551,44453,15439,41993,28373,32747,14381,45453,28133,28408,38874,33707,10653,34590,37389,16580,45030,44567,21018,33042,32374,46790,10004,40923,38856,3243,26835,20338,44789,5077,16021,39761,35710,12767,26269,25397,48846,14591,41036,27810,45613,39859,2694,34708,34455,49465,37423,48129,8464,13263,18904,20127,47848,29230,28446,40599,30037,36000,12686,209,16224,19991,40558,752,30858,32952,38497,20725,31156,24645,8818,15985,34588,10265,20837,7773,4187,22364,17707,12336,37597,14035,39908,29907,23804,26831,34886,40843,9795,31886,8118,2797,34066,27402,647,9610,42742,38606,10634,47291,19039,36033,8102,38852,5281,37131,4849,11995,13888,18034,20088,35747,48616,46515,32135,5300,25809,17507,32221,48396,15357,17429,29591,16162,31813,42287,49264,25709,9506,41866,7025,6070,27722,6278,2294,33643,21223,36274,15319,19029,5920,9281,3969,18862,36425,1244,1590,23489,67,2593,27203,48902,10920,2785,13684,4813,11397,13127,32186,5685,20585,30842,10914,29267,22661,46921,24383,6919,7543,35833,17621,49923,25013,31349,41208,39750,6596,37273,9353,12943,26461,30280,8364,49368,11089,47718,8566,2938,43409,37324,47923,5718,25473,4166,46011,17126,45715,34268,15401,45727,32842,46545,44042,28314,38574,23945,10805,26545,6662,29841,43101,31302,4930,27666,22834,19130,13507,25301,19118,10879,32968,16855,24773,30012,2394,34138,1782,36753,45500,16566,26498,10419,33029,34458,12497,36814,58,7216,29892,14523,16553,3811,15240,48250,32727,7219,24199,34427,32919,2997,33726,35602,3628,2140,41287,34395,30575,32407,43595,36922,27501,39507,47023,8064,31464,5439,7261,395,21096,29812,5905,21221,14332,11072,33643,46661,21698,5824,44995,42493,12018,9662,9066,25739,12891,645,17568,27865,25349,32933,8170,49859,39697,46999,42823,5517,10962,23453,2402,34191,22257,22367,46310,44805,9515,27372,34839,19205,34984,36854,17826,21205,13705,24982,11503,14888,10952,37146,794,7973,16435,39314,28126,19239,15185,38176,28331,40323,21824,21339,27314,837,29518,23292,33687,10465,37548,11692,5517,40016,36259,40662,19460,34084,47411,31894,17236,49246,29374,37578,11560,4355,48931,8204,33800,41920,6350,48238,39143,2575,1481,36829,22799,29683,16037,10215,44542,36367,8882,37514,15602,46205,28734,5061,44406,4546,45374,19857,26904,23805,8446,39842,19162,5104,18744,42386,49869,45005,34071,10883,1073,10329,46704,19240,31438,47507,48321,1077,28043,5026,30035,20943,7826,10605,11545,37991,41030,32620,9098,28844,37339,44302,33979,44897,31016,18550,25494,31702,15059,507,2354,42996,33874,27266,49705,31577,19205,27022,40082,32028,12551,26934,11258,17853,47064,5597,13819,16350,25807,22418,30269,22540,20657,6558,13401,34340,43448,11840,47761,18501,13415,22786,8177,19400,35489,4710,28886,24434,11169,727,13951,36899,6024,21531,5180,31556,35223,5551,39365,22232,6936,32219,46177,2505,47704,9524,30454,41406,36561,2215,449,21514,484,9303,13426,38851,26518,33199,18082,3624,40873,45401,44776,23647,35087,2410,45186,10570,5981,12176,32798,1301,8139,11030,4978,39655,42973,30289,16487,10605,16303,28814,16450,33175,24986,49265,5060,34583,35817,37447,17899,41216,15258,5878,40120,45664,17481,31563,28155,47104,34480,9948,5428,11252,43334,38163,11789,15691,44750,45770,9029,31503,19573,32910,20428,36909,37332,1580,41608,36769,44039,6578,9475,36101,38507,20072,45814,41294,30865,8183,47559,8860,1195,26836,42614,41718,20390,23073,19325,8092,4791,13789,30088,20890,24687,36081,43799,43814,39884,24342,5563,4934,42075,22604,48302,10479,9713,8751,1526,19294,41919,12944,40774,37647,34886,20309,41167,25390,28373,43100,13933,29392,45850,123,21634,41794,8657,774,36820,21700,5806,21352,12905,48072,3998,26499,358,35582,21001,27061,49330,8987,13479,19967,23334,10957,9032,38109,43189,8195,48983,34796,4552,38451,46153,28626,35444,40549,5991,23283,5339,41168,45832,34259,13659,5298,29465,30676,34212,44489,15458,43870,20383,16816,10556,1382,22694,29760,18242,34474,12809,46994,14798,2515,28561,31748,47387,42759,22313,29732,48797,17664,43568,4764,36154,31706,38898,41138,9023,48655,3913,22571,36003,34225,34336,38340,41992,7750,37941,18600,46971,30743,49943,35984,42182,17018,6526,36279,49115,18814,44400,14096,10193,37090,33931,17668,35547,14169,45085,35314,997,8908,4660,46588,11887,36920,5244,3225,27495,45815,2504,47647,21568,36024,30877,24613,46408,11903,30594,1478,47428,44364,23660,10554,40071,29563,31134,44542,37447,4933,28638,49748,44380,6341,9188,47171,11146,10187,41050,32323,27382,15032,1685,26280,24206,24892,41695,33566,5209,38898,9282,19750,899,49070,18351,20466,15505,21987,46260,26979,38722,10332,31333,16715,2980,22380,28676,28657,28575,21363,19263,14365,20965,43846,2749,19093,45567,35251,22719,25464,21135,6156,688,43344,34538,42532,13414,21050,25998,46838,37913,17093,765,42282,27124,30137,39468,6041,19734,18821,30031,29904,10681,10499,28580,699,25787,19919,29846,15142,16323,15317,30947,4719,15583,38060,44577,2619,6934,15709,8460,5223,16112,20409,20472,6105,34816,13278,39145,28658,43618,46697,37886,7595,39986,35795,7944,7880,35819,7086,30709,13193,19608,8900,2024,468,21542,6570,23018,32446,24946,14010,22791,39801,40568,32659,44952,38711,16744,43692,35460,33378,38497,32105,10501,18189,49794,11529,41967,28622,46839,36104,36596,39896,12680,3526,7000,15781,49054,8593,31016,36961,46410,27566,10474,45559,42833,44791,12954,48592,41934,19403,35834,28706,26556,36014,14496,27749,13612,33616,46819,31926,45162,1489,44211,18714,34829,34182,36556,40532,46003,8084,3334,20808,19829,7945,21066,9620,32393,31991,6868,20587,34089,41123,29880,45308,18150,5975,43112,40013,34556,33710,46287,7850,31022,29465,36722,33493,37141,6680,33049,12212,16797,27122,9674,40646,16172,28325,20060,37089,5274,34880,21047,38990,46906,38220,15129,35272,10584,7199,839,24169,23148,8286,44810,10295,19807,31759,13804,42249,23739,15983,13048,33184,37860,34937,37366,38426,12916,27903,28533,26069,19621,36018,14880,42355,482,31209,20841,48064,13405,13979,9,15991,48116,25094,16932,26657,46021,19741,3325,10543,45415,4677,29176,49969,8750,26593,9627,42288,28731,28063,9682,49623,20055,39496,24913,23243,14151,35283,18004,8610,3285,44081,36103,5006,2314,11022,43898,26766,3193,24536,31365,41928,2593,40122,40720,32427,47521,23187,12066,39479,23605,41467,215,24809,9246,13347,38187,22937,30196,49697,43858,5709,17714,33997,29374,39247,10034,25452,991,10321,38822,48014,15436,48716,13424,49349,17981,6969,24474,39245,19215,22259,45015,28384,40984,28251,20946,18595,43840,13851,12627,5498,28787,3565,48343,4990,17049,20063,18644,16444,27348,43717,45142,26877,4892,39173,5587,16314,30605,25305,43454,39781,9415,10356,27693,29298,22249,36776,42666,14151,33783,34531,40637,36913,12028,38769,27540,34983,42009,24707,40707,16632,27116,1269,991,7630,24482,34469,41079,7923,6975,49098,14651,41933,9639,20803,24110,25457,23058,30316,46933,31978,44846,44872,9253,5069,1789,31568,33320,2842,36985,33786,36232,31995,4098,3921,22992,4911,3017,32207,32722,39640,34040,7471,7359,19836,28374,31513,18740,2897,2943,23168,38272,39217,45983,14434,8017,42498,4335,48708,5216,43009,23444,47188,13477,21264,23023,40981,40225,3691,24873,30122,39972,37851,17438,42398,21595,28949,16802,24497,11460,48949,6108,26155,43974,27655,21545,35121,30932,13267,20380,39432,26835,16082,41887,10762,33988,7271,28259,25342,5386,41450,24156,34360,45331,298,8474,17082,26878,26362,22267,20100,16706,18402,21262,46162,5677,26491,39468,27074,15832,28566,48759,27947,12075,39884,5367,21213,18269,29754,17723,24381,4320,48644,43922,8406,5446,19741,13747,30414,12108,17103,28486,25893,951,17280,27565,26066,11288,36136,43690,44761,44631,35356,9310,40346,44358,35536,12584,12882,30636,5642,7522,1939,21000,48703,4449,27827,7414,6334,19799,41986,48583,34014,3535,5047,16106,7771,29351,40046,27689,40247,4451,47409,8605,21348,3526,20278,21619,2881,48789,34092,18586,18938,8540,28270,29294,15829,44898,24620,6435,23813,4339,15178,31337,11995,39657,29897,11044,8770,6756,22899,37760,41540,37223,1351,7659,49857,47988,16818,22006,34142,26374,9793,15331,5839,820,48424,18239,4002,14067,47826,36544,38025,40678,19879,4310,9671,8484,16039,36197,27673,16396,9001,41381,21587,26527,44141,34722,4387,43736,47270,30396,24735,27320,37153,15079,30652,26537,28593,33334,42928,3178,42817,8135,6546,27667,8001,34425,27792,29763,34310,8635,25479,37368,11003,12888,48285,34153,690,33944,19654,8673,4747,43396,30052,38101,49817,3924,43773,8780,8201,38421,1853,25843,35010,33660,33859,21037,36396,6829,21345,8024,45307,49706,38599,39583,13425,22745,38280,8102,8490,12583,19197,12040,42161,31862,19820,45930,3842,17606,21179,925,20083,23553,15666,48771,39219,18147,35740,13759,44172,47622,22180,17252,23652,29528,27467,29770,10516,15860,44123,37744,8087,45418,43252,12559,13212,32994,22319,45586,45709,2042,9903,14960,48886,45469,26434,15634,30772,16687,47824,12250,5989,8953,32364,34193,11853,17333,22989,19694,20073,31111,33933,14511,16137,44088,21025,8899,24423,35731,32274,21584,25126,12660,1909,10680,38608,48320,16656,4711,6287,14283,18460,23770,27427,40671,788,6290,28640,7799,21795,38685,36757,8296,2957,49512,2138,38841,46683,28825,1746,48796,16337,36131,19495,4429,37731,6050,45265,20329,9258,36664,20168,46280,24042,30677,13150,36140,23020,45129,47121,24681,34342,22064,2475,10051,41828,42886,31470,10704,4657,20880,12954,16840,48271,11800,42348,21805,25773,34666,13210,26631,2113,19780,30288,45435,46003,31599,31035,3573,44169,23134,32478,7637,45386,47636,29791,26753,6826,35383,2633,9093,4513,27518,19533,17890,13920,30101,10590,38619,41474,48822,21730,40661,3076,17426,16569,17388,8695,34036,7437,1304,2638,3258,32733,21027,31489,33018,22352,35583,22275,7244,44094,9586,24966,24128,28372,31168,25368,3903,32764,18300,44775,36535,42619,44547,4661,43467,14703,46250,23189,30208,48597,2573,42578,12891,4890,38064,17953,8943,45848,7299,29201,1186,16965,17945,34271,40558,46319,774,5561,33750,41915,21706,847,19994,9944,40823,43458,40086,21908,18428,32959,12046,49585,33051,18637,11202,19787,39581,31474,24173,14226,1322,10490,38971,41446,27078,48818,25590,27112,18455,49710,24881,15526,6667,8990,27695,30252,7756,878,11797,34565,33337,36833,49469,30848,15503,30468,26754,23526,41833,32059,35901,38029,35731,28998,47714,30080,14107,41474,14748,13928,602,3856,27122,33212,47065,7721,29863,10471,49691,24170,32044,8904,37953,15260,17834,22141,4995,20946,11688,28586,17302,39213,19024,27489,20729,33373,3675,44879,3353,46336,45634,5889,13369,27243,46940,16469,4015,41867,12135,39830,32191,49956,2622,44376,650,40448,40988,28106,31968,19329,17073,26105,31498,23097,23096,31629,35331,49934,42347,44509,1133,47065,33474,43070,43183,45235,20863,10156,14126,6156,25964,26342,44764,19191,28737,34037,29777,34871,42394,27784,39579,19983,28477,2508,26509,6302,8974,21610,21947,4443,33772,24309,31511,666,9961,19639,45540,42482,46541,30770,7174,48102,14004,13993,32202,23689,49946,34165,49106,26263,46445,34973,1886,9159,709,17054,14174,39022,49572,35465,10855,27607,5018,44886,17716,42204,23799,35560,17420,43945,49545,38186,47199,12876,35171,7380,44169,41687,43056,47327,17176,24037,18434,28278,10296,23183,9683,1562,3772,44002,14768,35357,8143,49113,19643,45950,27031,21681,31290,36905,48554,46388,48135,36042,21307,14680,13099,11227,13284,4611,44016,22428,45505,43609,39588,12161,7306,14733,4835,42354,34289,23352,38952,3625,23903,42083,24014,35658,17820,8497,12665,4284,9117,29181,29614,24499,43480,5203,18595,21975,15883,5089,27799,15698,3049,20931,17469,49231,35670,7015,35173,25389,6608,33431,18980,30959,7160,27141,18202,42375,8412,36181,49856,31347,46577,48833,25769,30560,19562,2343,10628,12363,12992,21672,2622,48604,35960,40905,16585,46790,1465,11209,14343,1547,26855,29178,15617,40852,22971,9753,15416,44026,25079,4139,15463,36034,33154,472,27451,43717,39886,3382,8585,9821,13504,32848,33983,16141,33361,7293,5756,22989,42217,6538,24452,12292,28536,47294,48072,26535,15151,39714,17632,17187,22051,23100,11972,28947,42296,28854,22367,32812,27273,11776,25491,33242,15702,36975,16722,47150,36670,9858,26691,10846,35502,2978,42794,47791,45838,26267,32705,12015,37005,11448,3257,14884,120]
        Output= 4321
        self.assertEqual(Output, get_sol().maxWidthRamp(nums))

    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):