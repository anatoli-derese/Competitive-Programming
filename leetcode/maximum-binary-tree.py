# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(i,j):
            if i >j:
                return None
            maxx = i
            for k in range(i,j+1):
                if nums[k] > nums[maxx]:
                    maxx = k
            node = TreeNode(nums[maxx])
            node.left = rec(i,maxx - 1)
            node.right = rec(maxx + 1, j) 
            return node
        return rec(0, len(nums)-1)       