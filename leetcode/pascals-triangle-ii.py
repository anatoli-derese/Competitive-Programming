class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        upper = self.getRow(rowIndex-1)
        i = 1 
        while i < len(upper):
            upper[i-1] =upper[i] + upper[i-1]
            i +=1
        upper.insert(0,1)
        return upper 

        