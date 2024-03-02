# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        holder = defaultdict(list)

        def rec(root,num,level):
            if not root:
                return 
            holder[level].append(num)
            rec(root.left , 2*num + 1, level + 1)
            rec(root.right, 2*num + 2, level + 1)
        rec(root,0,0)
        ans = 1
        for key in holder:
            ans = max(ans,
                max(holder[key]) - min(holder[key]) + 1
                )
        return ans
        