class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(cards) == len(set(cards)):
            return -1
        ans = float('inf')
        d = {}
        for i,num in enumerate(cards):
            if num in d:
                ans = min(i-d[num]+1, ans)
                d[num] = i
            else:
                d[num] = i
        return ans
        