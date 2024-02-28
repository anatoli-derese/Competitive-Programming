# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def zig(path, right):
            temp = []
            if not path:
                return
            for i in range(len(path)-1,-1,-1):
                node = path[i]
                if node:
                    if right:
                        temp.append(node.left)
                        temp.append(node.right)
                    else:
                        temp.append(node.right)
                        temp.append(node.left)
            ans.append(temp)
            if not temp:
                return 
            zig(temp, not right)
        ans.append([root])
        zig([root], False)
        finalAns = []
        for level in ans:
            temp =[]
            for node in level:
                if node:
                    temp.append(node.val)
            if temp:
                finalAns.append(temp)

        return finalAns
        