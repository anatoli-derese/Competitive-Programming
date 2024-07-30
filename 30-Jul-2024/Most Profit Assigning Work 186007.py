# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        tot = list(zip(difficulty, profit))
        heapify(tot)
        worker.sort()
        ans = 0
        maxx = 0
        for emp in worker:
            while tot and tot[0][0] <= emp:
                maxx = max(maxx, heappop(tot)[1])
            ans += maxx
        return ans
        
        