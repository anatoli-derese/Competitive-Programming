class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counts = defaultdict(int)
        acc = 0
        ans = 0
        for num in nums:
            acc += num
            if acc == goal:
                ans +=1
            ans += counts[acc-goal]
            counts[acc] +=1
        return ans

        


            