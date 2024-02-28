# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = []

        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            self.ans.append(root.val)
            inOrder(root.right)
        inOrder(root)
        print(self.ans)
        return self.ans[k-1]


        