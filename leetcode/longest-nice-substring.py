class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        temp = set(s)
        for i, c in enumerate(s):
            if c.swapcase() in temp:
                continue
            pre = self.longestNiceSubstring(s[0:i])
            post = self.longestNiceSubstring(s[i+1:])
            if len(pre)   >= len(post):
                return pre
            return post
        return s
        