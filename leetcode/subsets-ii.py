class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()
        def backtrack(i, path):
            if i > len(nums):
                return
            if path not in self.ans:
                self.ans.append(path[:])
            for j in range(i,len(nums)):
                path.append(nums[j])
                backtrack(j+1, path)
                path.pop()

        backtrack(0,[])

        return self.ans