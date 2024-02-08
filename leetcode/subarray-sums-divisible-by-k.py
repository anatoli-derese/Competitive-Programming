class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem = defaultdict(int)
        rem[0] = 1  
        acc = 0
        ans = 0
        for num in nums:
            acc += num
            ans += rem[acc % k]
            rem[acc % k] +=1
        return ans
            
            

        