class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        whole=len(set(nums))
        ct=1
        for k in range(whole, len(nums)):
            i,j = 0,k
            track=defaultdict(int)
            for x in range(j):
                track[nums[x]]+=1
            if len(track)==whole:
                ct+=1
            
            while j<len(nums):
                track[nums[i]]-=1
                if track[nums[i]]==0:
                    del track[nums[i]]
                track[nums[j]]+=1
                if len(track)==whole:
                    ct+=1
                i+=1
                j+=1
        return ct