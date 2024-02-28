# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        
        def rec(root):
            if not root:
                return
            rec(root.left)
            ans.append(root.val)
            rec(root.right)
        rec(root)
        return ans == sorted(ans) and len(ans) == len(set(ans))
        