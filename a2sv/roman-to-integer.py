class Solution:
    def romanToInt(self, s: str) -> int:
        #d ={"I":0, "V":0, "X":0, "L":0, "C":0 ,"D":0, "M":0}
        i = len(s)-1
        ans =0
        while i >= 0:
            if s[i] == "I":
                ans +=1
                i -=1
            if s[i] == "V":
                if i > 0 and s[i-1]=="I" :
                    ans +=4
                    i -=2
                else:
                    ans += 5
                    i -=1
            if s[i] == "X":
                if i > 0 and s[i-1]=="I" :
                    ans +=9
                    i -=2
                else:
                    ans += 10
                    i -=1
            if s[i] == "L":
                if i > 0 and s[i-1]=="X":
                    ans +=40
                    i -=2
                else:
                    ans += 50
                    i -=1
            if s[i] == "C":
                if i > 0 and s[i-1]=="X":
                    ans +=90
                    i -=2
                else:
                    ans += 100
                    i -=1
            if s[i] == "D":
                if i > 0 and s[i-1]=="C":
                    ans +=400
                    i -=2
                else:
                    ans += 500
                    i -=1
            if s[i] == "M":
                if i > 0 and s[i-1]=="C":
                    ans +=900
                    i -=2
                else:
                    ans += 1000
                    i -=1

        return ans