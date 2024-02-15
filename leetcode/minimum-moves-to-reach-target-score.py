class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        dbl = 0 
        while target > 1:
            if target % 2 == 0 and dbl < maxDoubles:
                dbl +=1
                target = target // 2
            else:
                target = target-1
            if dbl == maxDoubles:
                return ans + target 
            ans +=1
        return ans
        