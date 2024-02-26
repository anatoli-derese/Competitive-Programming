class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if k == len(cookies):
            return max(cookies)
        self.ans = float('inf')
        def backtrack(i, path,_max):
            if i >= len(cookies):
               self.ans = min(self.ans, _max)
               return
            if _max >= self.ans:
                return
            for person in range(k):
                path[person] +=cookies[i]
                backtrack(i+1, path, max(_max, path[person]))
                path[person] -= cookies[i]
        backtrack(0,[0]*k,0)
        return self.ans

            