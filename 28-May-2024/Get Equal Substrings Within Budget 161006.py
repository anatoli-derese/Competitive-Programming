# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        left = 0
        wind = 0
        ans = 0
        for right in range(len(diff)):
            wind += diff[right]
            while wind > maxCost:
                wind -= diff[left]
                left +=1
            ans = max(ans, right-left+1)
        return ans