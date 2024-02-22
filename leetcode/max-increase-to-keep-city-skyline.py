class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        """
        first create a way to store the maximums of each row and each column
        then iterate over the whole grid , increasing each cell to the minimum of the maxiums of the cols and the rows
        """      
        rowMax = defaultdict(lambda :-1)
        colMax = defaultdict(lambda :-1)
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                rowMax[i] = max(rowMax[i], grid[i][j])
                colMax[j] = max(colMax[j], grid[i][j])
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                ans += abs(grid[row][col] -min(rowMax[row], colMax[col]))
        return ans
