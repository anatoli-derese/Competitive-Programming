class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i  = float('inf')
        ans = ""  
        for s in strs:
            i = min(len(s), i)
        for j in range(i):
            temp = strs[0][j] 
            for  k in strs:
                if temp != k[j]:
                    return ans
            ans += temp
        return ans
            
        
        