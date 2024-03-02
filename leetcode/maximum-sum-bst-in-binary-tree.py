# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def rec(root):
            nonlocal ans
            if not root:
                return (float('inf'), float('-inf'), True, 0)
            
            if not root.left and not root.right:
                ans = max(ans, root.val)
                return (root.val,root.val, True, root.val)
            

            minLeft, maxLeft , leftBst, leftSum = rec(root.left)
            minRight, maxRight, rightBst, rightSum = rec(root.right)
            if (leftBst and rightBst) and (root.val > maxLeft and  root.val < minRight):
                ans = max(ans, leftSum+ rightSum + root.val)

                return (min(minLeft, root.val, minRight),
                    max(maxLeft, root.val, maxRight),
                    True,
                    leftSum+ rightSum + root.val )
            return (
                min(minLeft, root.val, minRight),
                    max(maxLeft, root.val, maxRight),
                    False,
                    0 
            )
        rec(root)
        return ans

        