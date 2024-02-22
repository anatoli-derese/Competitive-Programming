class Solution:
    def __init__(self):
        self.visited ={0:0, 1:1}
    def fib(self, n: int) -> int:
        if n in self.visited:
            return self.visited[n]
        
        first = self.fib(n-1)
        second = self.fib(n-2)
        self.visited[n] = first + second
        return first + second