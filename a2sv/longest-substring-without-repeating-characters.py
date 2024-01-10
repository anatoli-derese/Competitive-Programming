class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = 0
        window = defaultdict(int)
        i,j = 0,0
        while j < len(s):
            window[s[j]] +=1
            while window[s[j]] > 1:
                window[s[i]] -=1
                i +=1
            size = max(size, j-i+1)
            j +=1
        return size
            

        