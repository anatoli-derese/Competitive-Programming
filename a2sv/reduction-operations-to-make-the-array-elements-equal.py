class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        count = Counter(nums)
        i, j = len(nums)-2 , len(nums)-1
        ans = 0
        while i >= 0:
            if nums[i] != nums[j]:
                ans += count[nums[j]]
                count[nums[i]] += count[nums[j]]
            i -=1
            j -=1
        return ans



        