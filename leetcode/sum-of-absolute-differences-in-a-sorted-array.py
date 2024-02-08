class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pref =[]
        acc = 0
        for num in nums:
            acc += num
            pref.append(acc)
        leftSum = 0
        ans = []
        for i in range(len(nums)):
            rightSum = pref[-1] - pref[i]
            rightSum -= nums[i] * (len(nums)-i-1)
            if  i >=0 :
                amt = (i+1)*nums[i]
                leftSum = amt - pref[i]
            ans.append(leftSum+rightSum)
        return ans
            
