# Problem: Count Collisions of Monkeys on a Polygon - https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

class Solution:
    def monkeyMove(self, n: int) -> int:
        ans = (1<<n) - 2
        return ans % (10**9 + 7)