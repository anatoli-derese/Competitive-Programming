class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        ans = []
        for i in range(1, len(weights)):
            ans.append(weights[i] + weights[i-1])
        ans.sort()
        mx , mn = 0,0
        for i in range(k-1):
            mx += ans[~i]
            mn += ans[i]
        return mx - mn        