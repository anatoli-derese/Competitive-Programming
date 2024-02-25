class Solution:
    def balancedString(self, s: str) -> int:
        track = Counter(s)
        left = 0
        ans = float('inf')
        for right in range(len(s)):
            track[s[right]] -=1
            while left < len(s) and max(track.values()) <= len(s) / 4:
                ans = min(ans, right-left+1)
                track[s[left]]+=1
                left +=1
        return ans if ans != float('inf') else 0