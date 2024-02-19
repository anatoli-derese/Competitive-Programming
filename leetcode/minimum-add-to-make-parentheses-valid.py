class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened, closed = 0,0
        uncool = 0
        for char in s:
            if char == "(":
                opened +=1
                uncool +=1
            else:
                if opened > 0 :
                    uncool -=1
                    opened -=1
                else:
                    uncool +=1
        return abs(uncool)
        