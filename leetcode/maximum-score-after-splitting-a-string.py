class Solution:
    def maxScore(self, s: str) -> int:
        zc = []
        zac, oac = 0, 0
        oc = []
        for i in range(len(s)):
            if s[i] == "0":
                zac += 1
            if s[~i] == "1":
                oac += 1
            zc.append(zac)
            oc.append(oac)
        oc.reverse()
        ans = 0
        for i in range(len(s)-1):
            ans = max(zc[i]+ oc[i+1] ,ans)
        return ans


      
