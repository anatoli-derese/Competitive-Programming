# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.counts = defaultdict(int)
        def rec(root):
            if not root:
                return
            rec(root.left)
            self.counts[root.val] +=1
            rec(root.right)
        rec(root)
        temp = []
        maxx = max(self.counts.values())
        for num in self.counts:
            if self.counts[num] == maxx:
                temp.append(num)
        return temp

        