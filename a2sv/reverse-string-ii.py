class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        jumping = 0 
        ans = ""
        while jumping < len(s):
            ans += s[jumping: jumping+k][::-1]
            oj = jumping
            jumping += 2*k
            ans += s[oj + k:jumping]
        return ans


        