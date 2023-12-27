class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        area = -1
        points.sort()
        i,j = 0,1
        while j < len(points):
            temp = points[j][0]- points[i][0]
            area = max(area, temp)
            i +=1
            j +=1
        return area
        