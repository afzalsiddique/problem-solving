import unittest;


def get_sol(): return Solution()
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==1: return s[0]
        if n==2: return s if s[0]==s[1] else s[0]
        dp=[[0]*n for _ in range(n)] # boolean should be used. 0 or 1 used for debugging purposes

        for i in range(n):
            dp[i][i]=1
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=1
            else:
                dp[i][i+1]=0
        for i in range(n-2,-1,-1):
            for j in range(i+2,n):
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=dp[i+1][j-1]

        max_length=0
        max_i,max_j=-1,-1
        for i in range(n):
            for j in range(i,n):
                if dp[i][j] and j-i+1>max_length:
                    max_length=j-i+1
                    max_i,max_j=i,j
        return s[max_i:max_j+1]
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    dp[i][j]=True
                elif s[i]==s[j]:
                    if j-i+1==2:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]

        # for x in dp: print(x)
        maxx=float('-inf')
        start,end=-1,-1
        for i in range(n):
            for j in range(i,n):
                if dp[i][j]:
                    if j-i+1>maxx:
                        maxx=j-i+1
                        start,end=i,j
        return s[start:end+1]

class Solution3:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = ''
        for i in range(n):
            dp[i][i] = True
            ans = s[i]
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i + 1] = True
                ans = s[i:i+2]
        for left in range(n - 1, -1, -1):
            for right in range(left + 2, n):
                if s[left] == s[right] and dp[left+1][right-1]:
                    dp[left][right] = True
                    if right-left+1 > len(ans):
                        ans = s[left:right+1]
        return ans

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual('aba',get_sol().longestPalindrome('babad'))
    def test02(self):
        self.assertEqual('a',get_sol().longestPalindrome('a'))
    def test03(self):
        self.assertEqual('aa',get_sol().longestPalindrome('aa'))
    def test04(self):
        self.assertEqual('aaa',get_sol().longestPalindrome('aaa'))
    def test05(self):
        self.assertEqual('bacab',get_sol().longestPalindrome("abacab"))
    def test06(self):
        self.assertEqual('c',get_sol().longestPalindrome("ac"))
    def test07(self):
        self.assertEqual('bb',get_sol().longestPalindrome("cbbd"))
    def test08(self):
        self.assertEqual('aca',get_sol().longestPalindrome("aacabdkacaa"))
    def test09(self):
        self.assertEqual('oxaxo',get_sol().longestPalindrome("vmqjjfnxtyciixhceqyvibhdmivndvxyzzamcrtpywczjmvlodtqbpjayfchpisbiycczpgjdzezzprfyfwiujqbcubohvvyakxfmsyqkysbigwcslofikvurcbjxrccasvyflhwkzlrqowyijfxacvirmyuhtobbpadxvngydlyzudvnyrgnipnpztdyqledweguchivlwfctafeavejkqyxvfqsigjwodxoqeabnhfhuwzgqarehgmhgisqetrhuszoklbywqrtauvsinumhnrmfkbxffkijrbeefjmipocoeddjuemvqqjpzktxecolwzgpdseshzztnvljbntrbkealeemgkapikyleontpwmoltfwfnrtnxcwmvshepsahffekaemmeklzrpmjxjpwqhihkgvnqhysptomfeqsikvnyhnujcgokfddwsqjmqgsqwsggwhxyinfspgukkfowoxaxosmmogxephzhhy"))
    def test10(self):
        self.assertEqual('a',get_sol().longestPalindrome("abdka"))
    def test11(self):
        self.assertEqual('iffi',get_sol().longestPalindrome("jfbnhnjamsfsbsslcaaivnzryrrkcqmektqjnymeifxvvskicpxxrztysetlpucxfqccmeyptxxziqhacxatxjynmbblssyaxvcmbtyrtqfwxrwsgfrinfkczktytwglbrskeogamecvihkywnljnqfmrrnqcvopcoyroncwzhdqzvwdbtjmcocwljjvipabzorajqgiabqjeyasbrjvyjtdvgupqtmydfgdczaodyokxxarfboxifcltizhhntciffijclljvdfgpsojwmupgtrbquuzjdefnmxtcaborisjcsavucmuovlksonzvmmuvujzirioxdcadeioravjoyxhrqevfwmxacimtvbmfweqpvfijyuqrjfgejrnlmhvbbmbvviilsothgvaqgqtllonrqbsltwpikfrckdhttxzmbqmbhbjjwfddnrfwtafgjtuqyatkpcavokouftqwdzfclkckwzfwlozksgkrcyimvdhfrzlqqxnfhjkwfiewwqmbfyjdjematsvusmqxzwfyukqwlfzzyzlkqvgmq"))
    def test12(self):
        self.assertEqual('byyb',get_sol().longestPalindrome("twbiqwtafgjbtolwprpdnymaatlbuacrmzzwhkpvuwdtyfjsbsqxrlxxtqkjlpkvpxmlajdmnyepsmczmmfdtjfbyybotpoebilayqzvqztqgddpcgpelwmriwmoeeilpetbxoyktizwcqeeivzgxacuotnlzutdowiudwuqnghjgoeyojikjhlmcsrctvnahnoapmkcrqmwixpbtirkasbyajenknuccojooxfwdeflmxoueasvuovcayisflogtpxtbvcxfmydjupwihnxlpuxxcclbhvutvvshcaikuedhyuksbwwjsnssizoedjkbybwndxpkwcdxaexagazztuiuxphxcedqstahmevkwlayktrubjypzpaiwexkwbxcrqhkpqevhxbyipkmlqmmmogrnexsztsbkvebjgybrolttvnidnntpgvsawgaobycfaaviljsvyuaanguhohsepbthgjyqkicyaxkytshqmtxhilcjxdpcbmvnpippdrpggyohwyswuydyrhczlxyyzregpvxyfwpzvmjuukswcgpenygmnfwdlryobeginxwqjhxtmbpnccwdaylhvtkgjpeyydkxcqarkwvrmwbxeetmhyoudfuuwxcviabkqyhrvxbjmqcqgjjepmalyppymatylhdrazxytixtwwqqqlrcusxyxzymrnryyernrxbgrphsioxrxhmxwzsytmhnosnrpwtphaunprdtbpwapgjjqcnykgspjsxslxztfsuflijbeebwyyowjzpsbjcdabxmxhtweppffglvhfloprfavduzbgkw"))
    def test13(self):
        self.assertEqual('gjjg',get_sol().longestPalindrome("qgecuralerljmghebsvkdxatotpbiqmxdyetorjhtmcxbgddcqwktfbpnrthsnctdmchbqqhmgtalwslepvrzsylxvlidzryqrvyoisfeqveqxivnslrtvegctcfdgfojjbohgqxxhltgaxqsfcuitjkyopbafjukbgyvkwddgbvznnvejxjlhgktoowpqlluabvhmoqnibhqlpmqgvhjdxthbhmrfrxlmxnhvhxsezehmvtxpdohjbgmnbvvemqhgaxpvytqyjrifubommzoeuqdidnmambohgegyfftsahhpoivetithnfuzppprkpovpymhqardzlohjwrfiyxcnqgdwslavpepmhopcqdabhmqsoqxjswitkwzkoefhfydeartdhreiyzgummxpbtmrxcogmtwjrhdejprotvhzebdvrbedsieznynuaxqcvuegtefvxltovozpqjqocqvnxkesbewmfeacmrmgehyvrfksbbctcmxnbqnlvogjjgzotghxdrpdzyyrdbpvgusyreehfkqxzcgdekjtahubwvcuiktwdczjxacwuqxrtbhjsoqmbqorihykbzcxlyteoourrhheveamoidfxqudkzrpfftcpropwjeymetuibsdatmbvlmjghexejvplaysxbguijitfvrlkgayprkljshhvlonydoxbcuvbwacyeuvzfqqzmanfioyrybcdhkvlizdagpskdcaloglhluokblzgsppcbj"))
    def test14(self):
        self.assertEqual('tkckt',get_sol().longestPalindrome("xfsxwjqovpvchyjzdqphjsligzljscmzmjzelmbfnqpukbninfbbljouesngmbdyzhqysroeyagglkgorllkrcditzisqhihmithgjcpilkgfdxxqqjpqnoavgkjhojrldsyucfgtzimdbjehrxxqlpaqdddzismsodvternodzxusuehllpujmjjukrilrubbwzdjxbpmvmmwzbrxcxsjsqljjezgyzmsjpucghjxksdfyucpbvwloyhwevzgudhpspgtvsbjqlzmpequxthdonvbmjpeirttllvmtonqmbqxqtdkgichbfzkbhmhotqpkaeshhecshqjvdwgwkegmujwcnmseicesxddrvutxomsgjeylpqiuyezdccarsiprmoqgyifidxhufocfdrbnqczhtztutspaftwctsmynozhakqgvfsvoffyslhoaptkcktopabrxxwrcbyfftleaotwpoqvjjdzxwwqxjnyszjqwjsghkzpvirwnwgsofkjluyxzgboxybzhnmqhkwgltwdjgnemaaadvflrzdqmjufwyuwzoimnvhlxhxjywbopresdrepulsaaexdeddyzeosqfwlnovfpxothrcxhxnumnymofkkuxvclwvuhcelieengfbhvinckrpbjuuewnwvnrvimgmpsfdlcffpdfwmydgzdvluaejwalueygvvojfovuxwhlwojldfpieqqpoqfxhbkcnrtzrnbaagonnawwaqdzamhnvwdtoxlkexihvrqwwimjn"))
