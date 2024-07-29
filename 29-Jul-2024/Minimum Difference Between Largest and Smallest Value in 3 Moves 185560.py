# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        n = sorted(nums)
        diff1 = n[-1] - n[3]
        diff2 =  n[-2] -n[2]
        diff3 = n[-3] - n[1]
        diff4 = n[-4] - n[0]
        return min(diff1, diff2, diff3,diff4)
        