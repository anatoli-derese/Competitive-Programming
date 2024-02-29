class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        
        def backtrack(path, tot,j):
            # print(path)
            if tot == target:
                self.ans.append(path[:])
                # self.visited.add(tuple(path[:]))
                return
            else:
                for i in range(j,len(candidates)):
                    if i > j and candidates[i] == candidates[i-1]:
                        continue
                    tot += candidates[i]
                    if tot > target:
                        return 
                    path.append(candidates[i])
                    backtrack(path, tot, i+1)
                    tot -= candidates[i]
                    path.pop()
        backtrack([],0,0)
        # print(self.visited)
        return self.ans

        # 1,1,2,5,6,7,10