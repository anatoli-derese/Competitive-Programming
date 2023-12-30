class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = [0] * max(costs)
        for c in costs:
            count[c-1] +=1
        ans = 0
        for i, qty in enumerate(count):
            for _ in range(qty):
                if coins - (i+1) >= 0:
                    coins -= (i+1)
                    ans +=1
        return ans