# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/


class Solution:
    def minimumPushes(self, word: str) -> int:
        track = Counter(word)
        if len(track) <= 8:
            return len(word)
        turn = 1
        ans = 0
        unique = [i for i in track]
        unique.sort(key = lambda x : - track[x])
        i = 0
        while i < len(unique):
            t = unique[i]
            ans += track[unique[i]] * turn 
            i += 1 
            if not i%8:
                turn +=1
        return ans
            
            

        
        