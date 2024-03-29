class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if t==s:
            return s

        def checker(win,td):
            for i in td.keys():
                if i not in win:
                    return False
                if win[i] < td[i]:
                    return False
            return True
        td = defaultdict(int)
        win = defaultdict(int)
        for i in t:
            td[i] +=1
        l, temp = 0,""
        r,size =0,0
        while r < len(s):
            win[s[r]] += 1
            while checker(win,td):
                win[s[l]] -= 1
                if win[s[l]]==0:
                    del win[s[l]]
                size = r-l+1
                if size < len(temp) or len(temp)==0:
                    temp =s[l:r+1]
                    size = len(temp)
                l += 1
            r +=1
        return temp
            
        