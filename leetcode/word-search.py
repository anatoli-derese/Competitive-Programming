class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start = word[0]

        dirs = [
                (1,0),
                (-1,0),
                (0,1),
                (0,-1)
            ]

        
        
        def check(arr):
            for i in range(len(arr)):
                if arr[i] != word[i]:
                    return False
            return True
        
        def soFarBad (arr):
            for i in range(len(arr)):
                if arr[i] != word[i]:
                    return True
            return False
                
        
        self.ans = False
        
        def backtrack(x,y,path, vis):
            # print(path)
            if len(path) == len(word):
                if check(path):
                    self.ans = True
                return 
            if soFarBad(path):
                return 
            if self.ans:
                return 
            
            for dirX,dirY in dirs:
                startX = x + dirX
                startY = y + dirY
                if 0 <= startX < len(board) and 0 <= startY < len(board[0]):
                    if ((startX,startY) not in vis )and board[startX][startY] == word[len(path)]: 
                        path.append(board[startX][startY])
                        vis.add((startX, startY))
                        backtrack(startX, startY, path, vis)
                        path.pop()
                        vis.remove((startX, startY))
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == start:
                    temp = set()
                    temp.add((row,col))
                    backtrack(row,col, [board[row][col]], temp)        
        
        
        return self.ans
                    