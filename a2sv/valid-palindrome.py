class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        ans =""
        for letter in s:
            
            if (ord(letter) >= 97 and ord(letter)<=122) or (ord(letter)>= 48 and ord(letter)<=57) :
                ans+= letter
               
        
        back = ans[::-1]
        
        for i in range(len(ans)):
            print(ans[i],back[i])
            if ans[i] != back[i]:
                
                return False
        return True
            
        
        

        