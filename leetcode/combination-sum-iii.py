class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1,10)]
        self.ans = []
        target = n
        candidates.sort()
        
        def backtrack(path, tot,j):
            if len(path) == k and tot == target:
                self.ans.append(path[:])
                return
            else:
                for i in range(j,len(candidates)):
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