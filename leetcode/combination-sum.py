class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        self.visited = set()
        def backtrack(path, tot, vis):
            if tot == target:
                if tuple(sorted(vis)) not in self.visited:
                    self.ans.append(path[:])
                    self.visited.add(tuple(sorted(vis)))
                return
            else:
                for i in range(len(candidates)):
                    tot += candidates[i]
                    if tot > target:
                        return
                    vis.append(i)
                    path.append(candidates[i])
                    backtrack(path, tot,vis)
                    vis.pop()
                    tot -= candidates[i]
                    path.pop()
        backtrack([],0,[])
        return self.ans
        