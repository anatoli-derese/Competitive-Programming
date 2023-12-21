class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid[0])-2):
            for j in range(len(grid)-2):
                upper = sum(grid[j][i:i+3])
                mid = grid[j+1][i+1]
                lower = sum(grid[j+2][i:i+3])
                ans = max((upper+mid+lower), ans)
        return ans
        