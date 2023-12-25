class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primary = defaultdict(int)
        secondary = defaultdict(int)
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                primary[row-col] += mat[row][col]
                secondary[row+col] += mat[row][col]
        if len(mat) % 2 == 0: 
            return primary[0] + secondary[len(mat)-1]
        else:
            mid = len(mat) //2
            return primary[0] + secondary[len(mat)-1] - mat[mid][mid]

        