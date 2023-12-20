class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones = sum(nums)
        zeros = 0
        d = defaultdict(int)
        i = 0
        temp_max = 0
        while i <= len(nums):
            if i == 0:
                d[i] = ones
                temp_max = max(temp_max , ones)
            else:
                if nums[i-1] == 0:
                    zeros +=1
                    d[i] = zeros + ones
                    temp_max = max(temp_max , zeros+ ones)
                else:
                    ones -=1
                    d[i] = zeros + ones
                    temp_max = max(temp_max , zeros+ ones)
            i +=1
        ans = []
        for temp in d:
            if d[temp] == temp_max:
                ans.append(temp)
        return ans