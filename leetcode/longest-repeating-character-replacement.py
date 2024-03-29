class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        l,r,win,ans = 0,0,0,0
        while r < len(s):
            d[s[r]] +=1
            win = r - l + 1
            if win - max(d.values()) <=k:
                ans = max(ans,win)
            else:
                d[s[l]] -=1
                if d[s[l]] == 0:
                    del d[s[l]]
                l +=1
            r +=1
        return ans
        