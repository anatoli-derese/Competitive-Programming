class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = [[0]*len(image[0]) for _ in range(len(image))]
        for row in range(len(image)):
            for col in range(len(image[0])):
                if image[row][col] == 0:
                    ans[row][len(image[0])- col-1] = 1
        return ans