class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {s[i] : i for i in range(len(s))}
        ans = []
        size , end = 0,0
        for i, char in enumerate(s):
            size +=1
            end = max(end, d[char])
            if i == end:
                ans.append(size)
                size = 0
        return ans

        