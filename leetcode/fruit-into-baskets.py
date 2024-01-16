class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = defaultdict(int)
        left = 0
        ans = -1
        for right, num in enumerate(fruits):
            d[num] +=1
            while left< len(fruits) and len(d) > 2:
                d[fruits[left]] -=1
                if d[fruits[left]] == 0:
                    del d[fruits[left]]
                left += 1
            ans = max(ans, right-left+1)
        return ans
        