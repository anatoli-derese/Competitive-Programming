class Solution:
    def tellGrid(self,row,col):
        if row < 3 and col < 3:
            return "11"
        elif row < 6 and col < 3:
            return "41"
        elif row < 9 and col < 3:
            return "71"
        elif row < 3 and col < 6:
            return "14"
        elif row < 3 and col < 9:
            return "17"
        elif row < 6 and col < 6:
            return "44"
        elif row < 6 and col < 9:
            return "47"
        elif row < 9 and col < 6:
            return "74"
        else:
            return "77"

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        square = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                num = int(board[row][col])
                if num < 1 or num > 9:
                    return False
                if num in rows[row]:
                    return False
                rows[row].add(num)
                if num in cols[col]:
                    return False
                cols[col].add(num)
                pos = self.tellGrid(row,col)
                if num in square[pos]:
                    return False
                square[pos].add(num)
        return True
                
        

                    
        