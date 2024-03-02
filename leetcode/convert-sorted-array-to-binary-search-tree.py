# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(l,r):
            if l>=r:
                return 
            mid = (l +  ((l + r) // 2)) -l
            root = TreeNode(nums[mid])
            root.right = rec(mid+1, r)
            root.left = rec(l, mid)
            return root
        return rec(0, len(nums))
        
        