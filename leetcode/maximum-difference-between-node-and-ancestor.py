# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def rec(root, minn, maxx):
            if not root:
                return -1

            minn = min(root.val, minn)
            maxx = max(root.val, maxx)

            left = rec(root.left, minn, maxx)
            right = rec(root.right, minn, maxx)

            temp = max(maxx-minn, max(left,right))
            return temp
            
        return rec(root, float('inf'), float('-inf'))

        