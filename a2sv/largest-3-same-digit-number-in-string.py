class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = float('-inf')
        if len(num) < 3:
            return ""
        l,r = 0 , 2 # initialize the two pointers to take care of the window
        while r < len(num):
            if num[l:r+1].count(num[l]) == 3: # check if it has only one integer 
                ans = max(int(num[l:r+1]), ans)
            r +=1
            l +=1
        if ans == 0:
            return "000"
        elif ans == float('-inf'):
            return ""
        return str(ans)