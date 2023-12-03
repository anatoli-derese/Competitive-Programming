class Solution:
    def printVertically(self, s: str) -> List[str]:
        temp = s.split()
        lgst = 0
        indx = -1
        for i,word in enumerate(temp):
            if len(word) > lgst:
                indx = i
                lgst = len(word)
        ans = [""]*lgst
        for i in range(lgst):
            for j, word in enumerate(temp):
                if i < len(word):
                    ans[i] += word[i]
                else:
                    ans[i] += " "      
        for i in range(len(ans)):
            ans[i] = ans[i].rstrip()
        return ans