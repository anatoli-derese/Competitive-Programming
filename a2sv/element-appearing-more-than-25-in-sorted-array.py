class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        for i in count:
            if count[i]/ len(arr) > 0.25:
                return i        
        