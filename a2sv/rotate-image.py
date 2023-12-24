class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i , tpl in enumerate(zip(*matrix)):
            matrix[i] = list(tpl[::-1])

            
        