class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # holder = defaultdict(list)

        def rec(n,k):
            if n == 1:
                return 0
            parent = rec(n-1, math.ceil(k/2))
            if k % 2 == 0:
                return 1 if parent == 0 else 0
            else:
                return 0 if parent == 0 else 1
        return rec(n,k)
            
        