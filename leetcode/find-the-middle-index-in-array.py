class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pref = [0] * len(nums)
        for i in range(len(nums)):
            if i != 0:
                pref[i] = pref[i-1] + nums[i]
            else:
                pref[i] = nums[i]
        for i in range(len(nums)):
            if i == 0:
                if 0 == pref[-1] - pref[i]:
                    return i
            else:
                if pref[i-1] == pref[-1] - pref[i]:
                    return i
        return -1
        