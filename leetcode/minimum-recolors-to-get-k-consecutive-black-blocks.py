class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        wc = 0
        for i in range(k):
            if blocks[i] == "W":
                wc +=1
        ans = wc
        # print(ans)
        left = 0
        for right in range(k, len(blocks)):
            # print(ans, blocks[left:right+1])
            if blocks[left] == "W":
                wc -=1
            left += 1
            if blocks[right] == "W":
                wc +=1
            ans= min(wc, ans)
        return ans
            

