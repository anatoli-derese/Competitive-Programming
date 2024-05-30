# Problem: Find Building Where Alice and Bob Can Meet - https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(len(queries)):
            if queries[i][0] > queries[i][1]:
                queries[i][0], queries[i][1] = queries[i][1], queries[i][0]
            queries[i].append(i)
        queries.sort(key = lambda x: -x[1])
        ans =[-1]* len(queries)
        stack = []
        i = len(heights) - 1
        for x,y,ind in queries:
            if x == y or heights[x] < heights[y]:
                ans[ind] = y
                continue
            while i > y:
                while stack and heights[stack[-1]] < heights[i]:
                    stack.pop()
                stack.append(i)
                i -=1
            l,r = 0, (len(stack)-1)
            while l <= r:
                mid = l + (r-l)//2
                if heights[stack[mid]] <=  heights[x]:
                    r = mid - 1
                else:
                    l = mid + 1
            if 0<= r < len(stack):
                ans[ind] = stack[r]
        return ans
