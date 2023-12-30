class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        start , end = 0, len(piles)-1
        mine =  0
        while start <= end:
            mine += piles[end -1]
            end -=2
            start +=1
        return mine

        