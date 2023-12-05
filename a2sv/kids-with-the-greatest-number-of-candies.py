class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_temp = max(candies)
        result = []
        for num in candies:
            if num + extraCandies >= max_temp:
                result.append(True)
                max_temp 
            else:
                result.append(False)
        return result