class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp = set(nums)
        maximum = 0
        for i in nums:
            if (i - 1)  not in temp:
                length = 0
                while i + length in temp:
                    length +=1
                maximum = max(length, maximum)             
        return maximum

        