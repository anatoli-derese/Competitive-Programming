class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        def backtrack(i, path):
            if i > len(nums):
                return
            self.ans.append(path[:])
            for j in range(i,len(nums)):
                if nums[j] not in path:
                    path.append(nums[j])
                    backtrack(j+1, path)
                    path.pop()

        backtrack(0,[])

        return self.ans

        