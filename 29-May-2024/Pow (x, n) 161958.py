# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n ==0:
            return 1
        elif n ==1:
            return x
        elif n ==-1:
            return 1/x
        half= self.myPow(x,n//2)
        return half*half* self.myPow(x,n%2)
