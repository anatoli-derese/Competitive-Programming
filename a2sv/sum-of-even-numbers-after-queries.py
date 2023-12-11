class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for i in nums:
            if i % 2 == 0:
                even_sum += i
        ans =[]
        for val, indx in queries:
            if nums[indx] % 2 == 0:
                even_sum -= nums[indx]
            nums[indx] += val
            if nums[indx] % 2 == 0:
                even_sum += nums[indx]
            ans.append(even_sum)
        return ans
