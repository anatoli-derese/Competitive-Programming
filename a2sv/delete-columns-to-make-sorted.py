class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        min_len = float('inf')
        for s in strs:
            min_len = min(len(s), min_len)
        count = 0
        for i in range(min_len):
            l,r = 0, 1
            while r < len(strs):
                if strs[r][i] < strs[l][i]:
                    count +=1
                    break
                l +=1
                r +=1
        return count