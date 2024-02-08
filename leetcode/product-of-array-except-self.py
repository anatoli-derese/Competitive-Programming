class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = []
        back = []
        acc = 1
        bacc =1
        for i in range(len(nums)):
            acc *= nums[i]
            bacc *=nums[~i]
            front.append(acc)
            back.append(bacc)
        back.reverse()
        ans =[]
        for i in range(len(nums)):
            if i == 0:
                ans.append(back[i+1])
            elif i == len(nums) -1:
                ans.append(front[i-1])
            else:
                ans.append(front[i-1]*back[i+1])
        return ans
        