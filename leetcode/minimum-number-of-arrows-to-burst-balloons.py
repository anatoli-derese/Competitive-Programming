class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        end = float('-inf')
        ans = 0
        for left, right in points:
            if left <= end:
                end = min(end, right)
            else:
                ans +=1
                end = right
        return ans


        