class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome )== 1:
            return ""
        ans =""
        flag = False
        for i,char in enumerate(palindrome):
            if i == (len(palindrome) / 2) - 0.5:
                ans += char 
            elif not flag and char != "a":
                ans += "a"
                flag = True
            elif not flag and i == len(palindrome)-1:
                ans += "b"
            
            else:
                ans += char
        return ans
        

                
        