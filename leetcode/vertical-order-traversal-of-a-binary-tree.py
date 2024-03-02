# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        holder = defaultdict(list)
        vals = []
        def rec(root, row,column):
            if not root:
                return 
            vals.append((row,column))
            holder[(row,column)].append(root.val)
            rec(root.left,row+1, column - 1)
            rec(root.right, row+1, column + 1)
        rec(root, 0,0)
        vals = list(set(vals))
        vals.sort(key= lambda x: (x[1], x[0]))

        for key in holder:
            if len(holder[key]) > 1:
                holder[key] = sorted(holder[key])
        
        ans = []
        i = 0
        while i < len(vals):
            row, col = vals[i]
            temp =[]
            temp.extend(
                holder[vals[i]]
            )
            i += 1
            while i< len(vals) and col == vals[i][1]:
                temp.extend(
                    holder[vals[i]]
                )
                i += 1
            ans.append(temp)
        return ans