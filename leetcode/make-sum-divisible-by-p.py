class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rem = sum(nums) % p
        if rem == 0:
            return 0
        d = {}
        d[0]= -1
        acc = 0
        ans = float('inf')
        for i, num in enumerate(nums):
            acc += num 
            if ((acc%p)- rem)% p in d:
                ans = min(i-d[((acc%p)- rem)% p],ans)
            d[acc%p] = i
        return -1 if ans == float('inf') or ans == len(nums) else ans
        
