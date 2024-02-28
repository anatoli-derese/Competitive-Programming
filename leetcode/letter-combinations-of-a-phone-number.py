class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2' : "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        ans =[]
        
        def backtrack(i, path):
            if i == len(digits) == len(path) and path :
                ans.append("".join(path))
                return 
            
            for j in range(i, len(digits)):
                word = dic[digits[j]]
                for char  in word:
                    path.append(char)
                    backtrack(j+1, path)
                    path.pop()
        backtrack(0,[])
        return ans
