class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        ans = []
        cols, diag1, diag2 = set(), set(), set()

        def backtrack(row):
            if row == n:
                temp = []
                for r in board:
                    temp.append("".join(r))
                ans.append(temp)
                return
            for col in range(n):
                if col in cols or (row-col) in diag1 or (row+col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)
                board[row][col] ="Q"
                backtrack(row+1)
                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)
                board[row][col] = "."
        backtrack(0)
        return len(ans)
