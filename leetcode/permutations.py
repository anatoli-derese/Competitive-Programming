class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def backtrack(path):
            if len(path) == len(nums):
                self.ans.append(path[:])
                return
            for i in range(0, len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
        backtrack([])
        return self.ans


    