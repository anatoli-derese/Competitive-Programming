class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        for  num in nums:
            counter[num] +=1 
        ans =[]
        for i in counter:
            if counter[i] > len(nums)//3:
                ans.append(i)
        return ans
        