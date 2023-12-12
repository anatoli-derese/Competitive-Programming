class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        temp = s.split(" ")
        
        ans = ""
        for i in range(len(temp)-1,-1,-1):
            if temp[i] == " " or temp[i]=="":
                continue
            ans += temp[i].strip() +" "
        ans=ans.strip()
        return ans
        