class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        ans =""
        for letter in s:
            if letter.isalnum():
                ans += letter
        i,j = 0,len(ans)-1
        while i < j:
            if ans[i] != ans[j]:
                return False
            i +=1
            j -=1
        return True
            
        
        

        