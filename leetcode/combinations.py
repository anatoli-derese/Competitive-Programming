class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(num, path):
            if len(path) == k:
                ans.append(path[:])
                return 
            if num > n:
                return 
            path.append(num)
            backtrack(num+1, path)
            path.pop()
            backtrack(num+1, path)    

        ans = []
        backtrack(1,[])
        return ans 
        