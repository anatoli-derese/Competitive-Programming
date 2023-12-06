class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans =[0] * len(s)
        for i,num in enumerate(indices):
            ans[num] = s[i]
        return "".join(ans)