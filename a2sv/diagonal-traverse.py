class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        temp = defaultdict(list)
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                temp[row+col].append(mat[row][col])
        count = 0
        ans =[]
        for c in temp:
            if count > 1:
                if count % 2 == 0:
                    ans+=temp[c][::-1]
                else:
                    ans+=temp[c]
            else:
                ans+= temp[c]
            count +=1
        
        return ans