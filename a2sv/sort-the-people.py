class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {heights[i]: i for i in range(len(heights))}
        heights.sort(reverse =True)
        print(heights)
        ans =[]
        for i in range(len(names)):
            ans.append(names[d[heights[i]]])
        return ans
