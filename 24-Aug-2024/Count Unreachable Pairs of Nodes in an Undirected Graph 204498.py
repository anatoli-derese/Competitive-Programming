# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parents = {i:i for i in range(n)}
        rank  = defaultdict(int)

        def find(x):
            if x == parents[x]:
                return x
            parents[x] = find(parents[x])
            return parents[x]
        
        def connect(x,y):
            rootX,rootY = find(x) , find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parents[rootY] = rootX
                else:
                    parents[rootX] = rootY
                    rank[rootY] +=1
        
        for u,v in edges:
            connect(u,v)
        
        track = defaultdict(int)
        for node in range(n):
            track[find(node)] +=1
        arr = []
        for x in track:
            arr.append(track[x])
        # print(len(arr))
        tot = sum(arr)
        ans = 0
        # print(arr, tot)
        
        for i,val in enumerate(arr):
            if i != len(arr)-1:
                rest = tot - val
                tot -= val
                ans += rest * val
        return ans
        
        
 
        