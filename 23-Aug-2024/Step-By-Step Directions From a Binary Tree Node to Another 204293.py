# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        parent = {}
        def add(node, child):
            if not child:
                return 
            parent[child] = node
            add(child,child.left)
            add(child, child.right)
        add(root,root.left)
        add(root, root.right)
        
        path = {}
        
        start = ""
        def getStart(node):
            nonlocal start
            if not node:
                return 
            if node.val == startValue:
                start = node
                return 
            getStart(node.left)
            getStart(node.right)
        getStart(root)
        
        path = {}
        que = deque([start])
        end =""
        
        while que:
            node= que.popleft()
            if node.val == destValue:
                end = node.val
                break
            if node.left and node.left.val not in path:
                path[node.left.val] =[node.val ,"L"]
                que.append(node.left)
            if node.right and node.right.val not in path:
                path[node.right.val] = [node.val, "R"]
                que.append(node.right)
            if node in parent and parent[node].val not in path:
                path[parent[node].val] = [node.val, "U"]
                que.append(parent[node])
        
        ans = ""
       
        while end != start.val:
            end,dire = path[end]
            ans += dire
        
        return ans[::-1]


            


        
        