# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.inorder =[]
        self.postorder =[]
        def inOrder(root, depth):
            if not root:
                self.inorder.append(-101)
                return
            inOrder(root.left, depth +1)
            self.inorder.append((root.val, depth ))
            inOrder(root.right, depth+1)
        def postOrder(root,depth):
            if not root:
                self.postorder.append(-101)
                return
            postOrder(root.right,depth+1)
            self.postorder.append((root.val, depth))
            postOrder(root.left, depth+1)
        inOrder(root.left, 0)
        postOrder(root.right,0)
        # print(self.inorder, self.postorder)
        return self.inorder == self.postorder
        
    