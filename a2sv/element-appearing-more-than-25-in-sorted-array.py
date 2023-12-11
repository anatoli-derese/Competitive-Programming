class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d = defaultdict(int)
        total = len(arr)
        for i in arr:
            d[i] +=1
        for i in d:
            if d[i] / total > 0.25:
                return i
        
        