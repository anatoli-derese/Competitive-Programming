class Solution:
    
    def addChecked(self,area, guards):
        for row,col in guards:
            # to the right, the row is constant , only the columns change
            y = col + 1
            while y < len(area[0]):
                if area[row][y] == "W" or area[row][y] =="G":
                    break
                area[row][y] ="M"
                y +=1
            # to the left the row is still constant, only the columns decrease
            y = col - 1
            while y >= 0:
                if area[row][y] == "W" or area[row][y] =="G":
                    break
                area[row][y] = "M"
                y -=1
            # down, the columns is constant, the  row increases
            x = row + 1
            while x < len(area):
                if area[x][col] =="W" or area[x][col] =="G":
                    break
                area[x][col]= "M"
                x +=1
            # up, const. column, row dec
            x = row -1
            while x >=0:
                if area[x][col] =="W" or area[x][col] =="G":
                    break
                area[x][col]= "M"
                x -=1
        return area

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        area =[[0]* n for _ in range(m)]
        for x,y in guards:
            area[x][y] ="G"
        for x,y in walls:
            area[x][y] ="W"
        area = self.addChecked(area, guards)
        ans = 0
        for row in range(len(area)):
            for col in range(len(area[0])):
                if area[row][col] == 0:
                    ans +=1         
        return ans
        