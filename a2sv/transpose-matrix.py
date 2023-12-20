class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row , col= len(matrix), len(matrix[0])
        ans = [[0]*row for _ in range(col)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                ans[c][r] = matrix[r][c]
        return ans
    
        