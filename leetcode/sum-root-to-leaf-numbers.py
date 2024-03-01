# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans  = 0
        
        def rec(node , num):
            nonlocal ans
            if not node.right and not node.left:
                num += str(node.val)
                ans += int(num)
                return 
            if node.left:
                rec(node.left, num+ str(node.val))
            if node.right:
                rec(node.right, num+ str(node.val))
        rec(root,"")
        return ans                
        