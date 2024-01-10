class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[:k])
        wind = ans      
        i, j =0, k
        while j < len(nums):
            wind += nums[j]
            wind -= nums[i]
            ans  = max( wind, ans)
            i +=1
            j +=1
        return ans/k
        