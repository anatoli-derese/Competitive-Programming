class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        whole=len(set(nums))
        ans = 0
        tracker = defaultdict(int)
        left = 0
        for right in range(len(nums)):
            tracker[nums[right]] +=1
            while len(tracker) == whole:
                ans += len(nums) - right
                tracker[nums[left]] -=1
                if not tracker[nums[left]]:
                    del tracker[nums[left]]
                left +=1
        return ans