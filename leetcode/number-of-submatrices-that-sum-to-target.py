class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        prefixMatrix =[[0]* len(matrix[0]) for _ in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == 0 and col == 0:
                    prefixMatrix[row][col] = matrix[0][0]
                elif col == 0:
                    prefixMatrix[row][col] = prefixMatrix[row-1][col] + matrix[row][col]
                elif row == 0:
                    prefixMatrix[row][col] = prefixMatrix[row][col-1] + matrix[row][col]
                else:
                    prefixMatrix[row][col] = prefixMatrix[row-1][col] +prefixMatrix[row][col-1] - prefixMatrix[row-1][col-1]+ matrix[row][col]
        ans = 0
        for r1 in range(len(matrix)):
            for r2 in range(r1, len(matrix)):
                count = defaultdict(int)
                count[0] = 1
                for c in range(len(matrix[0])):
                    curr = prefixMatrix[r2][c] - (
                        prefixMatrix[r1-1][c] if r1 > 0 else 0
                    ) 
                    diff = curr - target
                    ans += count[diff]
                    count[curr] +=1
        return ans

        