class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        line = [0] * len(nums)
        for start, end in requests:
            line[start] +=1
            if end  + 1 < len(nums):
                line[end+1] -=1
        for i in range(1,len(line)):
            line[i] += line[i-1]
        line.sort()
        nums.sort()
        ans = 0
        for i in range(len(line)):
            ans += nums[i] * line[i]
        return ans % ((10**9) + 7 )
        