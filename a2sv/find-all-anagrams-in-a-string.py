class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return[]
        parr = [0]*26
        sarr = [0]*26
        for i in p:
            parr[
                ord(i) - ord('a')
            ] +=1
        for i in range(len(p)):
            letter = s[i]
            sarr[ord(letter) - ord("a")] +=1
        ans = []
        if sarr == parr:
            ans.append(0)
        i, j = 1,len(p) 
        while j < len(s):
            sarr[ord(s[i-1]) - ord('a')] -=1
            sarr[ord(s[j]) - ord('a')] +=1
            if parr == sarr:
                ans.append(i)
            i +=1
            j +=1

        return ans

        