class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a":0,"e":0,"i":0,"o":0,"u":0 }
        for i in range(k):
            if s[i] in vowels:
                vowels[s[i]] += 1
        i, j = 1,k
        ans = sum(vowels.values())
        while j < len(s):
            if s[i-1] in vowels:
                vowels[s[i-1]] -=1
            if s[j] in vowels:
                vowels[s[j]] +=1
            i +=1
            j +=1
            ans = max(ans , sum(vowels.values()))
        return ans  
            
            
        