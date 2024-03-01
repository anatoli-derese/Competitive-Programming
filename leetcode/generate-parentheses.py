class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        def backtrack(temp, closed, opened):
             
            if closed > opened:
                return
            if len(temp) == 2 * n:
                ans.append("".join(temp))
                return
            if opened < n:
                temp.append("(")
                backtrack(temp, closed, opened+1)
                temp.pop()
            # if closed > n:
            #     return

             
         
            temp.append(")")
            backtrack(temp, closed + 1, opened)
            temp.pop()
        backtrack([],0,0)
        return ans