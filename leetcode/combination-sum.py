class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        self.visited = set()
        def backtrack(path, tot, i):
            if tot == target:
                self.ans.append(path[:])
                return
            else:
                for j in range(i,len(candidates)):
                    tot += candidates[j]
                    if tot > target:
                        return 
                    path.append(candidates[j])
                    backtrack(path, tot, j)
                    tot -= candidates[j]
                    path.pop()
        backtrack([],0,0)
        return self.ans
        