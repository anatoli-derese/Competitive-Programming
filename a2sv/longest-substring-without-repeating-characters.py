class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start,end, longest = 0, 0 ,0
        ans =[]
        while end < len(s):
            if s[end] not in ans:
                ans.append(s[end])
                longest = max(longest,end-start + 1 )
                end += 1
            else:
                ans.pop(0)
                start +=1
                longest = max(longest, end - start+1)
        return longest