# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped =[]
        for i,num in enumerate(nums):
            t =""
            for c in str(num):
                t += str(mapping[int(c)])
            mapped.append([int(t), i])
        mapped.sort()
        ans =[]
        for num, idx in mapped:
            ans.append(nums[idx])
        return ans