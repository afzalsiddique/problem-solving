from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/sum-of-subarray-ranges/discuss/1626628/O(n)-solution-with-monotonous-stack-oror-Full-explaination
    def subArrayRanges(self, A: List[int]) -> int:
        def fn(op):
            """Return min sum (if given gt) or max sum (if given lt)."""
            ans = 0
            st = []
            for i in range(n):
                while st and op(A[st[-1]], A[i]): # op(nums[st[-1]], nums[i])) -> nums[st[-1]]<nums[i] if op==left
                    j = st.pop()
                    k = st[-1] if st else -1
                    ans += A[j] * (i - j) * (j - k)
                st.append(i)
            while st:
                j = st.pop()
                k = st[-1] if st else -1
                ans += A[j] * (n - j) * (j - k)
            return ans
        n=len(A)
        return fn(lt) - fn(gt)
class Solution2:
    # https://leetcode.com/problems/sum-of-subarray-ranges/discuss/1626628/O(n)-solution-with-monotonous-stack-oror-Full-explaination
    def subArrayRanges(self, A: List[int]) -> int:
        def fn(op):
            """Return min sum (if given gt) or max sum (if given lt)."""
            ans = 0
            st = []
            for i in range(len(A) + 1):
                while st and (i == len(A) or op(A[st[-1]], A[i])): # op(nums[st[-1]], nums[i])) -> nums[st[-1]]<nums[i] if op==left
                    j = st.pop()
                    k = st[-1] if st else -1
                    ans += A[j] * (i - j) * (j - k)
                st.append(i)
            return ans

        return fn(lt) - fn(gt)
class Solution3:
    # not good
    def subArrayRanges(self, nums: List[int]) -> int:
        n=len(nums)
        res=0

        for i in range(n):
            minn,maxx=float('inf'),float('-inf')
            for j in range(i,n):
                minn=min(minn,nums[j])
                maxx=max(maxx,nums[j])
                res+=maxx-minn
        return res
class Solution4:
    #tle
    def subArrayRanges(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for win in range(2,len(nums)+1):
            inc=deque()
            dec=deque()
            for i in range(win-1):
                while inc and inc[-1][0]>nums[i]:
                    inc.pop()
                inc.append((nums[i],i))
            for i in range(win-1):
                while dec and dec[-1][0]<nums[i]:
                    dec.pop()
                dec.append((nums[i],i))
            for i in range(win-1,n):
                while inc and inc[-1][0]>nums[i]:
                    inc.pop()
                inc.append((nums[i],i))

                while dec and dec[-1][0]<nums[i]:
                    dec.pop()
                dec.append((nums[i],i))

                res+=dec[0][0]-inc[0][0]

                while inc and inc[0][1]<=i-win+1:
                    inc.popleft()
                while dec and dec[0][1]<=i-win+1:
                    dec.popleft()

        return res



class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, get_sol().subArrayRanges([1,2,3]))
    def test2(self):
        self.assertEqual(4, get_sol().subArrayRanges([1,3,3]))
    def test3(self):
        self.assertEqual(59, get_sol().subArrayRanges([4,-2,-3,4,1]))
    def test4(self):
        self.assertEqual(978842485419133, get_sol().subArrayRanges([846695286,892227453,-281148211,-756938513,-666036926,532020333,880988745,916028277,285799306,384654670,188134663,-944772512,-242591874,-51467838,-297112568,843992195,-424837554,727440776,-991116872,-980781579,458058403,-678770063,-108579335,-989172308,-741290887,-876001561,301479745,850321695,-75791909,-167776312,-988559528,798052597,-929860892,219085800,876348705,151649048,429367880,819655132,-589156278,866242039,874247256,-453629090,137366688,-331881278,261148935,248005682,646069331,-940656796,-264436737,-629753025,-952350778,-496787108,482656374,662028488,645765229,-90254118,-372713545,999042520,-728695818,-194110819,31885520,966873947,-342194205,876597801,-847249255,526451028,-512915124,390591384,-689510449,829669441,486141456,164964664,-430920322,-884654257,55106789,324057636,-488788793,-993102957,964343255,352814359,-980188836,-440904663,308137030,-991516992,530172423,-583598911,669976172,555946430,-196524693,419887846,-283487261,210401356,526149739,-446647405,-927576142,852345918,-453213310,710274547,-573989952,-621190748,149065385,-29554919,289077344,96364152,529268068,881726790,489630354,957554858,636671589,-564638549,-914794232,960309857,708324298,-173561622,544950514,303694103,-65652210,442320241,710659928,646066527,92097966,-446404761,-528037017,-922602706,-286273184,-312278568,-41227865,-377083074,-802487882,416553183,506396757,536617447,-571947024,794965565,-186589130,-864385051,951362891,442217241,-516721049,-603543666,-327945466,571210964,-597406579,-648636927,516031688,883592118,779133097,444443011,-439672491,248058679,231910684,40964496,-622663029,-894199043,762513763,-259026406,-258608356,-154306128,-318915818,129969028,-865058299,-275793945,519114400,613026414,-959836925,-925064067,653681278,394174256,-413306240,206796261,238528358,980364295,-564206972,-805657409,613904440,19054666,173652872,-300235354,-704717475,-652498130,205693505,-17644788,286400744,-641166277,-590110754,-997079503,82871923,-707851708,34040630,-652722954,879543926,-612747248,242507472,793093688,-504809315,-635542900,-821696914,660923341,-813750552,292264051,629904477,552531744,-55385244,-76362719,-470359196,364940251,864571017,-601826798,248110291,-26829434,964856450,-232109184,699840744,214339327,633442697,528890450,243541087,992323282,-413668631,-429370763,439371870,-410725042,-459454842,-719142285,301576208,-935318750,163461348,-963772669,-698925678,-42795546,16447878,-301786293,754380767,759468409,-714169650,-608710678,-652858856,-373990739,-288220546,-328211434,-365111355,-179776418,-687768251,855724689,-134255657,742107628,842248796,490371895,-990419238,-104521896,539596043,-833817164,111467723,-232063062,647322433,560161258,256047437,-718793820,202471351,-547037718,-229555001,696067427,348004592,-120889260,-885402888,-662682643,-426676998,-180981664,-956783899,387477500,-958883155,-820543748,312184106,-732992582,-495224851,146721194,335037740,-842570032,23781117,665442958,318989302,153883132,790098026,19614778,-798319178,41809305,144101357,-623984027,426529343,-444745787,-654504124,389517764,550644843,-595713761,476495783,926710211,-14142678,-304709870,477432930,797373129,624385248,685743627,-618569470,-509615881,-978643977,-910324508,811708677,122274567,-798168167,-786661799,-877877670,-921719957,-210702171,-138441259,178634170,389874295,688381247,-442591009,-192100843,-75638083,-495717126,-946896171,95014276,-618393722,-359831606,-815753261,-629917691,-436531250,557424255,-893919188,-338231260,682337255,-301845712,234375159,-508090948,-820788995,482895612,83066356,924549960,642106341,464505620,-189105073,-397133801,463867822,27427338,-218379477,540489640,92131248,-850956721,465727519,273451736,127356596,11451807,-203184065,-4419815,546380626,166360595,468578800,424223632,150556555,-983176078,622249591,869488513,737035311,-761976805,781037522,324728157,70060469,623686770,734056338,655088926,-104211693,18088171,124075577,134647144,-189132533,-731166938,-355878440,-562851830,730260442,-345601733,477473873,-237567100,-693663361,-959119112,180248904,28680860,-310437466,236111651,-866330430,-217079550,54868594,669171505,-945907622,-173939218,735024462,-44166780,-993362048,624532613,510601988,-247600422,-459895245,-980157405,-277144119,406393656,-500871041,-692049805,-996281000,-376773883,865198118,-8643551,-33953976,-109728538,989318946,397331929,160959868,-62160471,340995329,497159051,-576591104,-593912230,651692987,-445372388,863897169,-451873647,-104509737,-367329997,-931906099,-338201752,352208666,-73678033,-41782295,-783764046,746267258,672944700,-336394424,-688408569,-180535435,108035756,529042601,-46088065,-351200228,566171597,220083736,-476892902,293871466,-436037658,484386537,33718606,446244425,281368521,-137843736,-759308982,-288308391,258311078,701522942,-843730517,-697753316,-762769600,119922184,479397453,170462293,-735707007,-262673194,585531483,-686125239,492909845,516232350,-484476018,-297678096,162123688,-600980028,982028924,-775275789,-880613265,-235181502,-578922096,-431255880,-594574637,409012495,-502664533,70150531,-345106104,-422998324,-626767829,-516073616,-397219897,386047277,-808336966,-769039761,-834323605,25024309,293711205,26388280,867592778,-289512408,929993073,94416494,-688947341,-309708706,48047566,612658892,-75218636,153277051,188838364,78623397,770134931,-158323559,115164788,-442949957,104596358,670489110,-905983343,-784195153,191839904,710434502,302866036,880000507,732795,950723869,923762737,-180888351,243352820,869177486,357460956,-221060140,-102244477,592777686,-261997735,783240697,733335995,-760578295,766900143,574451087,890856066,-636317679,-429517183,653391347,-542480977,-417451893,770606895,522406411,-293077718,340338253,-302371080,-207560461,904784254,-496381469,-904159617,-832960537,-970070610,149417718,-987203124,-797670630,-825102188,-615038202,881132709,-110987288,639384006,-783327167,472857655,-78080973,350140300,-34145673,-495933300,917418703,-343983603,-24506395,334103764,-19677643,-16298479,907114811,690940733,385195756,18534759,264335202,-130830269,-509993798,-162215458,237568040,905093022,109314140,-316053386,-615085965,148765829,148512011,138686259,583690744,602454583,680669590,682577283,820830077,-699295648,-448204197,-195641147,292578672,-634148163,-262370167,96923326,-656467385,888015270,-643476434,948970182,680787406,406624557,-962963422,666218361,-736284239,269637598,311266018,972490631,-666285385,-42061842,-202868510,188644005,-791631903,-786834238,-185607357,812438867,-748792836,-347355071,711547341,-735288775,-523878849,310981662,-665882089,113789085,459150256,328978703,734199177,-346689471,-141705677,-722231217,-824080156,559265145,119411538,-390087556,86542739,-830747469,466185031,469766889,-343098240,542790488,77820861,725997943,548448066,-199243470,-939883449,742669754,32545232,784940465,403786933,289246097,-457202069,-446078798,46913323,-496950170,-677647077,781711462,-997152381,-854907368,-895178214,-129367091,626058000,330573768,-957811217,-40549529,-367275222,-343688773,409106689,723993911,-113049359,924040790,-527294295,-306973028,929855068,967697402,885779066,166016472,-566431274,706936605,805561201,8043980,-326644122,113966617,-199069763,-473755859,-283666300,-750464873,654391258,-969442829,-525107772,-399756421,544957242,757630892,471824223,542934161,488928250,-332234538,-941469419,-721529248,-119213174,365881320,-38611405,336290170,536057348,643955387,474016443,-685111148,-529245453,-622433214,595092198,471678812,-584967920,450111541,-825289859,509104376,530233770,-887720151,378868822,119103591,-617315130,222033125,-327797302,-734619431,935629401,175613116,-870196854,-795917612,509244362,-500296246,-298708324,417597390,-172003209,75015857,433540542,-907132667,-120417849,-975063887,720576125,-784484479,874189120,-138664940,408583264,980437192,-431716267,-473143055,10702399,556256783,-997285026,-175316532,903386818,589107702,982890491,-995533386,512519225,-468165659,564202966,-617782571,-394158844,796398076,-858636578,945053304,535568520,276252417,401293658,440118108,-848508672,-771509748,254814060,185492217,-990612207,-233720691,-445804541,588561959,946306590,-422175331,-778506464,231016412,304988427,327427546,582744529,650182355,891479778,-607929415,727987908,-171291868,-74096482,-670732537,-21128028,461475592,-986899709,860375310,915702852,-198720753,-561710740,-553178598,908472134,-30559143,209068538,-916149142,-789481201,-212225585,638316592,886586393,-77036999,-910946028,298246055,600880863,136409645,461820848,725516219,461126547,-309013952,350217141,-800291024,693067660,-127547939,89630043,-637986724,-410915793,-648905127,-625733750,516160455,-12369734,312117917,332910125,-615775063,857715048,-831355709,-429537133,-92005475,637883829,-973549811,-441593543,-237934128,-152203222,85978104,-982436636,-36229682,-341533861,963865894,-494466521,-136651078,644428827,-637348611,-880222152,-570351745,-741268177,-42373094,-169849095,147319025,163242686,391819347,-433280794,136627971,827833798,-531672043,-248126912,-57270697,-313701405,728239237,-469028832,-680806286,987775239,185000245,-622658787,223656121,957591612,748953290,869658490,652332178,-41081978,-697436690,653499783,-588475108,871291364,540431459,582280813,-560173610,-120362433,-990574362,-182130046,-245106899,614253202,907974707,-552279408,-881387584,700598954,296944756,-742894985,-830808536,-440232208,-30496657,-707638993,189582350,261794542,-299891610,100587847,-957182197,-929876013,-981950086,-93719052,790878493,678432171,667352287,36449499,443726410,-697126276,749415473,914628558,-394162418,64855939,-486435310,651692465,-728061365,145344426,-435114402,33292523,652704360,393587026,-86507650,358545953,-622760739,-378084692,-700032227,-331780918,544637773,-739763083,-859976553,709853472,-60592866,-5588063,171071353,-720092385,54784911,733546921,-641624603,972600542,-98203807,-730947906,850223955,586039987,399522369,-880983846,899310613,554552544,-906343781,-765623812,692153281,-862078355,187327321,676673332,978451260,-223508848,-581866672,-789425727,708199488,-52586902,-485112520,-651872621,63913403,-126759619,437171004,-973432053,-767211883,-524412694,-744298767,168332421,-505469582,864674677,-564370427,-837875073,-70704897,595909329,-704893808,-652522125,68044794,523039023,716743946,-302437918,-583388593,-133641331,-441928305,51264013,856903261,-329161228,871995352,15723732,-319417669,278304122,-264389407,699803247,-839703592,419830258,655801407,668264104,-434930351,885533838,-499717724]))
    def test5(self):
        self.assertEqual(40, get_sol().subArrayRanges([4,6,1,3,5]))
    # def test6(self):
    # def test7(self):
