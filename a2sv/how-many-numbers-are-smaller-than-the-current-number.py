class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)
        ans = []
        for num in nums:
            ans.append(
                bisect.bisect_left(sorted_num, num)
            )
        return ans