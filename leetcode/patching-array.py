class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        curr = 0
        ans = 0
        for num in nums:
            if curr >= n:
                return ans
            while curr + 1 < num:
                curr += curr + 1
                ans +=1
                if curr >= n:
                    return ans
            curr += num
        while curr < n:
            curr += curr + 1
            ans += 1 

        return ans

            
            


            

        