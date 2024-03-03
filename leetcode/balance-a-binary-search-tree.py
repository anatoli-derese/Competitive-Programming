# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        ans = []
        def inOrder(root):
            if not root:
                return 
            inOrder(root.left)
            ans.append(root.val)
            inOrder(root.right)
        def construct(l,r):
            if l >=r:
                return None
            mid = ((l + r)//2) 
            node = TreeNode(ans[mid])
            node.left = construct(l,mid)
            node.right = construct(mid+1, r)
            return node
        inOrder(root)
        # print(ans)
        return construct(0, len(ans))
        