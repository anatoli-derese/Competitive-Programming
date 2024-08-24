# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo ={}

        def dp(row,index):
            if row == len(triangle) -1 : # last row
                return triangle[row][index]
            if (row,index) in memo:
                return memo[(row,index)]
            direct = triangle[row][index] + dp(row+1, index)
            left = triangle[row][index] + dp(row+1, index + 1)
            memo[(row,index) ] = min(direct, left)
            return memo[(row,index)]
        
        return dp(0,0)