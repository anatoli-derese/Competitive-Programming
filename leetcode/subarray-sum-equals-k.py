class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        track = defaultdict(int)
        acc = 0
        ans = 0
        for i in range(len(nums)):
            acc += nums[i]
            nums[i] = acc
            if acc == k:
                ans +=1
            if acc - k in track:
                ans += track[acc-k]
            track[acc] +=1
        print(nums)            
        return ans