class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        inds = defaultdict(list)
        for i, num in enumerate(nums):
            inds[num].append(i)
        ans =[0]* len(nums)
        for val in inds:
            pref = list(accumulate(inds[val]))
            for i,k in enumerate(inds[val]):
                right, left = 0,0
                if i < len(pref)-1:
                    right = pref[-1] - pref[i]  - (k * (len(pref)-1-i))
                if i > 0:
                    left = k*(i) - pref[i-1]
                temp = right + left
                ans[k] = temp
        return ans
 
        